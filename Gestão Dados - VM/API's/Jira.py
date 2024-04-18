import pandas as pd
import requests as r
import numpy as np
import time
import json

# Funções para tratamento de dados
def apply_rule(row):
    if row['Status Sprint'] in [None, 'closed'] and row['Categorias'] != 'Epic' and row['Status'] not in ['Concluído', 'final']:
        return 'BACKLOG'
    else:
        return row['Sprint']


def apply_status(row):
    if row['Sprint'] in ['BACKLOG']:
        return 'active'
    else:
        return row['Status Sprint']
    
# Informações do Projeto
id_projeto = "10012"

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
    
## Colunas coletadas na API    
# Resumo da Tarefa
fields = [indice['fields'] for indice in issues]
resumo = [indice['summary'] for indice in fields]

# Nome Sprint
sprint = [indice['customfield_10020'][-1]['name'] if indice.get('customfield_10020') else None for indice in fields]

# Status Sprint
stt_sprint = [indice['customfield_10020'][-1]['state'] if indice.get('customfield_10020') else None for indice in fields]

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
    "Status Sprint": stt_sprint,
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

# Criando Data Frame
df = pd.DataFrame(data_dict)

# Retirando todos os epicos coletados
df = df[df['Categorias'] != 'Epic']

# Tratando as colunas Sprint's    
df['Sprint'] = df.apply(apply_rule, axis=1)
df['Status Sprint'] = df.apply(apply_status, axis=1)