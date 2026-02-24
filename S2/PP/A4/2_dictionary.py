# Criando um dicionário de uma pessoa
pessoa = {
    "nome": "João da Silva",
    "idade": 35,
    "email": "joao.silva@email.com", 
    "telefone": "+55 11 99999-8888"
}

print(pessoa)
#saida
# {‘nome’: ‘João da Silva’, ‘idade’: 35, 
# ‘email’: ‘joao.silva@email.com’, ‘telefone’: ‘+55 11 99999-8888’}


"""
Podemos armazenar de forma conectada chaves dentro de chaves
Para acessar basta mencionar as chaves em ordem de profundidade
"""

pessoa = {
'nome': 'João da Silva', 'idade': 35,
'email': 'joao.silva@email.com', 
'telefone': '+55 11 99999-8888',
'endereco': {
'rua': 'Av. Paulista', 
'numero': 1234, 
'cidade': 'São Paulo', 
'estado': 'SP',
'cep': '01311-200'
},
'documentos': {
'cpf': '123.456.789-00',
'rg': '12.345.678-9'
}
}

# Exemplo de acesso aos dados 
print(pessoa['nome'])	# Saída: João da Silva
print(pessoa['endereco']['cidade'])	# Saída: São Paulo
print(pessoa['documentos']['cpf'])	# Saída: 123.456.789-00

## Alterando valor de uma chave
pessoa['idade'] = 36	# Atualizando um valor existente 
pessoa['cidade'] = 'São Paulo' # Adicionando uma nova chave


"""
Para remover itens de um dicionário podemos utilizar o comando del
especificando a chave a ser removida, também podemos retirar a chave 
mas ficar com o valor retornando ele para uma var, ex:
"""
del pessoa["email"]	# Remove uma chave específica print(pessoa)

email = pessoa.pop("email")	# Remove e retorna o valor associado
print(email)	# Saída: joao.silva@email.com


## Percorrendo dicionários
# Percorrendo chaves e valores
for chave, valor in pessoa.items(): print(f"{chave}: {valor}")

"""
O dicionário possui em sua estrutura métodos nativos (funções implementadas
para a estrutura específica) que facilitam a manipulação, tal como os métodos 
keys() (retorna todas as chaves), values() (retornam todos os valores) e items() (retorna 
todos os itens).
"""

print(pessoa.keys())	# Retorna todas as chaves 
print(pessoa.values()) # Retorna todos os valores 
print(pessoa.items())	# Retorna pares chave-valor 

if "email" in pessoa:
    print("E-mail cadastrado:", pessoa["contato"]["email"])
