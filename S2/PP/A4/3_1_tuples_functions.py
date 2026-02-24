## Tuplas como parâmetro
def exibir_dados_pessoais(dados):
    nome, idade, cidade = dados	# Desempacotamento da tupla 
    print(f'Nome:  {nome},  Idade:  {idade},  Cidade:  {cidade}')

# Criando uma tupla com dados
pessoa = ('João da Silva', 35, 'São Paulo')

# Passando a tupla como argumento 
exibir_dados_pessoais(pessoa)

# saída
# Nome: João da Silva, Idade: 35, Cidade: São Paulo


## Retorno de tuplas por função
def calcular_idade_futura(idade_atual, anos):
    idade_futura = idade_atual + anos
    return  idade_atual,  idade_futura	# Retorno como tupla

idade_atual, idade_futura = calcular_idade_futura(35, 5) 

print(f'Idade atual: {idade_atual}, Idade em 5 anos: {idade_futura}')

#saida
# Idade atual: 35, Idade em 5 anos: 40

## Em tuplas temos o mesmo comportamento que listas, onde é passado como referência
def exibir_dados_pessoais(dados):
    print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")

pessoa = {
'nome': 'João da Silva', 'idade': 35, 'cidade': 'São Paulo'
}

exibir_dados_pessoais(pessoa) #saida
#Nome: João da Silva, Idade: 35, Cidade: São Paulo

print(f"Essa é o dicionário pessoa -> {pessoa} que foi modificada pela função!")

## Outro exemplo com modificação
def   adicionar_email(pessoa): 
    pessoa["email"] = "joao.silva@email.com"

dados_pessoais = {"nome": "João da Silva", "idade": 35}
adicionar_email(dados_pessoais)

print(dados_pessoais) 
#saida
# {'nome': 'João da Silva', 'idade': 35, 'email': 'joao.silva@email.com'}

## Copiando o dicionário para que não modifique o original
def adicionar_email(pessoa): 
    nova_pessoa = pessoa.copy()
    nova_pessoa['email'] = 'joao.silva@email.com' 
    return nova_pessoa

dados_pessoais = {'nome': 'João da Silva', 'idade': 35} 
dados_modificados = adicionar_email(dados_pessoais)

print(dados_pessoais)	# Original não é alterado 
print(dados_modificados) # Novo dicionário com a modificação