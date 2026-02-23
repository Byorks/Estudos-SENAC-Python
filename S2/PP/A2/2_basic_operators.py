"""
Serão apresentados exemplos de inserção, remoção, alteração e busca de elementos em uma lista
"""

## Inserindo no final da lista
numeros = [10, 20, 30]
numeros.append(40) # Adiciona 40 no final 
print(numeros)

## Inserindo em posição específica
numeros = [10, 20, 30]
numeros.insert(1, 15)	# Insere 15 na posição 1 
print(numeros)

## Inserindo vários elementos 
numeros = [10, 20, 30]
numeros.extend([40, 50, 60])	# Adiciona múltiplos valores ao final
print(numeros)


# Removendo elementos

## Removendo a primeira ocorrência inserida no parâmetro 
numeros = [10, 20, 30, 40, 30, 50]
numeros.remove(30)	# Remove a primeira ocorrência de 30
print(numeros)

## Removendo a partir do índice
numeros = [10, 20, 30, 40, 50]
del  numeros[1]	# Remove o elemento no índice 1 (20)
print(numeros)

## Limpando a lista
numeros = [10, 20, 30, 40, 50]
numeros.clear()	# Esvazia a lista
print(numeros)

## Alterando um valor específico da lista
numeros = [10, 20, 30, 40, 50]
# Alterar o elemento no índice 2 (de 30 para 35)
numeros[2] = 35
print(numeros)


## Verificando por items na lista
numeros = [10, 20, 30, 40, 50]
# Verifica se 30 está na lista
if 30 in numeros:
    print("30 está na lista")

numeros = [10, 20, 30, 40, 50]

# Buscar manualmente
for i in range(len(numeros)):
    if numeros[i] == 30:
        print('Encontrado no índice:', i)
        break
