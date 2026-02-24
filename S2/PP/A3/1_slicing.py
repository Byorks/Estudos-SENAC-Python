# ---- Slicing (Fatiamento) ----

"""
Exemplo
lista[início:fim:passo]

Em que:

 -início é o índice do primeiro elemento a ser incluído no fatiamento (opcional; padrão é 0).

 - fim é o índice do primeiro elemento a ser excluído do fatiamento (opcional; padrão é o tamanho da lista).

 - passo define a variação entre os índices extraídos (opcional; padrão é 1).
"""

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublista  =  numeros[2:7]	# Do índice 2 ao 6
print(sublista)	# Saída: [2, 3, 4, 5, 6]


# Pegando números de forma alternada, estamos pegando um sim e um não gerando na lista com pares
# Isso porque o terceiro parâmetro são quantos steps/passos vamos pegar o slice
# Nesse caso a lista toda foi pega, mas apenas a cada dois passos
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = numeros[::2]	# Pegando elementos com passo 2
print(pares)	# Saída: [0, 2, 4, 6, 8]

# Também é possível fazer o slicing invertido
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
invertida  =  numeros[::-1]	# Passo negativo para inverter
print(invertida)	# Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Substituindo valores em uma lista
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[2:5] = [20, 30, 40]	# Substituindo elementos
print(numeros)	# Saída: [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Removendo itens da lista a partir do índice
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del numeros[2:5] # Remove os elementos do índice 2 ao 4
print(numeros) # Saída: [0, 1, 5, 6, 7, 8, 9]

"""
Ao fazer slicing, ter em mente que ele duplica a lista, portanto para grande armazenamento de dados
o ideal é procurar alternativas mais eficientes
"""