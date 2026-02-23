"""
JSON lib já vem embutido no Python.
Temos as seguintes funções para trabalhar com arquivos JSON.
"""

# json.dumps() # Converte um dicionário Python para uma string JSON
# json.loads() #converte uma string JSON para um dicionário Python
# json.dump() # escreve dados JSON em um arquivo
# json.load() # lê dados JSON de um arquivo e os converte em um objeto Python


import json

# Dicionário Python - chave e valor
dados = {
    "nome": "Poliana",
    "idade": 26,
    "cidade": "Campinas"
}

with open("dados.json", "w") as arquivo: # w -> write
    json.dump(dados, arquivo, indent=4)
    
print("Dados salvos com sucesso!")
    
with open("dados.json", "r") as arquivo: # r -> read
        dados_carregados = json.load(arquivo)
        
print("Dados carregados:", dados_carregados)