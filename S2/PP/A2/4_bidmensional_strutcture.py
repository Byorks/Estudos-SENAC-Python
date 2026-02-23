# ---- Estruturas bidimensionais ----

"""
No exemplo a seguir, listas nativas são utilizadas para representar uma matriz de três linhas e três colunas:
A contagem também inicia no 0.
"""

# Criando uma matriz 3x3 usando listas aninhadas
matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
# Acessando um elemento específico (linha 1, coluna 2)
print(matriz[1][2]) # Saída: 6

# Definição de uma matriz 3x3 
matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

# Percorrendo a matriz linha por linha for linha in matriz:
for elemento in matriz: print(elemento, end="")
print()	# Nova linha para organizar a saída
