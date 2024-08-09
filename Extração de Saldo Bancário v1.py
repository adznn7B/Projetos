import pandas as pd
import pdfplumber

def clean_numeric_columns(df, columns):
    for column in columns:
        # Remove pontos de milhar e substitui vírgula por ponto, depois converte para float
        df[column] = df[column].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
        df[column] = pd.to_numeric(df[column], errors='coerce')  # Converte para numérico (float)
    return df

# Caminho para o arquivo PDF
pdf_path = 'C:\\Users\\adrie\\Documents\\GitHub\\Projetos\\CONTAS_1.pdf'

# Lista para armazenar os dados extraídos
tables = []
header_saved = False

# Usar pdfplumber para extrair tabelas do PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        for table in page.extract_tables():
            if not header_saved:
                # Use o primeiro cabeçalho e armazene-o
                df = pd.DataFrame(table[1:], columns=table[0])
                header_saved = True
            else:
                # Use as colunas já definidas, ignorando os cabeçalhos subsequentes
                df = pd.DataFrame(table[1:], columns=tables[0].columns)
            
            # Limpar colunas numéricas
            df = clean_numeric_columns(df, ['Crédito (R$)', 'Débito (R$)'])
            
            tables.append(df)

# Concatenar todas as tabelas em um único DataFrame
final_df = pd.concat(tables, ignore_index=True)

# Salvar o DataFrame consolidado em um arquivo Excel
output_path = 'C:\\Users\\adrie\\Documents\\GitHub\\Projetos\\contas_extrato_final.xlsx'
final_df.to_excel(output_path, index=False)

print(f"Arquivo Excel gerado com sucesso em: {output_path}")