import pandas as pd
import requests as r
import numpy as np
import time
import json

# Informações do Projeto
id_projeto = "10012"
id_tarefa = ""

# Informações para Autenticação da API
url = "https://vianaemoura.atlassian.net"
token = "ATATT3xFfGF0LKHC3Gd-ZvodTFGFNZXN-Yib4maQWjpoH7V9A7eXDTVGTGoYKDpKuZnjXR4WiMx5mj-WTfMwKmWx1brR298nYpTRG6OICeIzJpvaM3QitxcC37Ym1bSp7bKw6D4J7tBm-T6poIZUwvKF27w-Sho69UW1qi9I4cwhj5RwdtvZ3XE=FF3ACEFA"
login = "adrielsena@vianaemoura.com.br"

# Dados da API
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

query = url + "/rest/api/3/search?jql=project=10012"

# Requisição
issues = []
start_at = 0
while True:
    query = f"{url}/rest/api/3/search?jql=project={id_projeto}&startAt={start_at}&maxResults=50"
    response = r.request("GET", query, headers=headers, auth=r.auth.HTTPBasicAuth(login, token))
    data = json.loads(response.text)
    issues.extend(data['issues'])
    if start_at >= data['total']:  # Verifica se já foram recuperados todos os itens
        break
    start_at += 50
    
# Resumo da Tarefa
fields = [indice['fields'] for indice in issues]
resumo = [indice['summary'] for indice in fields]

# Nome Sprint
sprint = [indice['customfield_10020'][0]['name'] if indice.get('customfield_10020') else None for indice in fields]

# Data da Criação da Tarefa
data_criacao = [indice['created'] for indice in fields]

# ID da Tarefa
id = [indice['id'] for indice in issues]

# Chave da Tarefa
key = [indice['key'] for indice in issues]

# URL da Tarefa
url = [indice['self'] for indice in issues]

# Prioridade da Tarefa
prioridade = [indice['priority']['name'] for indice in fields]

# Responsável pela Tarefa
responsavel = [indice['assignee'] for indice in fields]

# ID Pai
id_pai = [indice['parent']['id'] if 'parent' in indice and indice['issuetype']['subtask'] else None for indice in fields]

# Chave Pai
key_pai = [indice['parent']['key'] if 'parent' in indice and indice['issuetype']['subtask'] else None for indice in fields]

# Tags/Categorias
#categorias = [indice['labels'] for indice in fields]
categorias = [indice['issuetype']['name'] for indice in fields]

# Status da Tarefa
status = [indice['status']['name'] for indice in fields]

# Total de tarefas no projeto
total_de_issues = data['total']

# Horas previstas do card
prev = [indice['customfield_10033'] for indice in fields]


# Criando Data Frame
data_dict = {
    "Chave da Tarefa": key,
    "ID da Tarefa": id,
    "Nome da Tarefa": resumo,
    "Sprint": sprint,
    "Data de Criação": data_criacao,
    #"URL da Tarefa": url,
    "Prioridade": prioridade,
    "Responsável": [resp['displayName'] if resp is not None else None for resp in responsavel],
    "ID do Pai": id_pai,
    "Chave do Pai": key_pai,
    "Categorias": categorias,
    "Status": status,
    "Horas Previstas": prev
    #"Total de Tarefas": total_de_issues
}

# Salvando as issues em um arquivo JSON
#with open('issues.json', 'w') as f:
#    json.dump(issues, f, indent=4)

df = pd.DataFrame(data_dict)

# Especificar o caminho e o nome do arquivo
#caminho_do_arquivo = 'dados_jira.xlsx'

# Exportar o DataFrame para Excel
#df.to_excel(caminho_do_arquivo, index=False)  # index=False para não incluir o índice como uma coluna no arquivo Excel

#print(f'Arquivo exportado com sucesso para {caminho_do_arquivo}')

