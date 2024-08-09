import pandas as pd
import pdfplumber
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import re

# Variável global para armazenar o caminho do arquivo selecionado
selected_file_path = None

def extract_accounts_from_pdf(file_path):
    accounts = set()
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                matches = re.findall(r"Conta:\s(\d+-\d+)", text)
                if matches:
                    accounts.update(matches)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao extrair contas: {str(e)}")
    return sorted(accounts)

def clean_numeric_columns(df, columns):
    for column in columns:
        df[column] = df[column].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def process_pdf(file_path, selected_account):
    try:
        tables = []
        extracting = False
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                
                # Verificar se a conta selecionada está na página
                if f"Conta: {selected_account}" in text:
                    extracting = True  # Iniciar extração quando a conta for encontrada
                
                # Continuar extraindo até que a conta mude ou até o final do relatório
                if extracting:
                    for table in page.extract_tables():
                        # Verificar se a conta mudou no meio do processo
                        if f"Conta:" in text and f"Conta: {selected_account}" not in text:
                            extracting = False
                            break
                        
                        # Processar a tabela
                        df = pd.DataFrame(table, columns=table[0])
                        df = clean_numeric_columns(df, ['Crédito (R$)', 'Débito (R$)'])
                        tables.append(df)
                
                # Parar a extração se encontrar um cabeçalho de uma nova conta
                if not extracting:
                    break

        if tables:
            final_df = pd.concat(tables, ignore_index=True)
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            output_path = os.path.join(desktop, f'contas_extrato_{selected_account}.xlsx')
            final_df.to_excel(output_path, index=False)
            messagebox.showinfo("Sucesso", f"Arquivo Excel gerado com sucesso em: {output_path}")
        else:
            messagebox.showinfo("Informação", "Nenhuma tabela encontrada para a conta selecionada.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def select_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo PDF",
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        selected_file_path = file_path
        accounts = extract_accounts_from_pdf(file_path)
        if accounts:
            account_var.set(accounts[0])  # Seleciona a primeira conta por padrão
            account_dropdown['values'] = accounts
            process_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Erro", "Nenhuma conta encontrada no PDF.")

def start_processing():
    if selected_file_path:
        selected_account = account_var.get()
        process_pdf(selected_file_path, selected_account)
    else:
        messagebox.showerror("Erro", "Nenhum arquivo foi selecionado.")

# Criar a interface gráfica
root = tk.Tk()
root.title("Conversor de PDF para Excel")

canvas = tk.Canvas(root, height=200, width=400)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1, relheight=1)

label = tk.Label(frame, text="Selecione o arquivo PDF:")
label.pack(pady=10)

select_button = tk.Button(frame, text="Escolher Arquivo", padx=10, pady=5, command=select_file)
select_button.pack()

account_var = tk.StringVar()
account_dropdown = ttk.Combobox(frame, textvariable=account_var, state="readonly")
account_dropdown.pack(pady=10)

process_button = tk.Button(frame, text="Processar", padx=10, pady=5, state=tk.DISABLED, command=start_processing)
process_button.pack()

root.mainloop()