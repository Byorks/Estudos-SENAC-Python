"""
No Python temos a cópia rasa (Shallow Copy) e a cópia profunda (Deep Copy)

A copia rasa não vai criar um novo objeto para objetos que estão inseridos dentro 
de onde estamos copiando, e isso pode gerar problemas

O que isso quer dizer, o simples  copy() vai usar os objetos internos como referência,
então alterar eles na cópia, altera no original

Exemplo:
"""
import copy

lista_a = [[1, 2, 3], [4, 5, 6]]

# Criando uma cópia profunda do elemento aninhado(que está dentro) da lista_a
lista_b = copy.deepcopy(lista_a)
# primeiro param é a primeira lista e o segundo é o primeiro elemento da primeira lista
lista_b[0] [0] = "batata"
print("lista A:", lista_a)
print("lista B:", lista_b)


lista_a = [[1, 2, 3], [4, 5, 6]]

# Criando uma cópia rasa do elemento aninhado(que está dentro) da lista_a
lista_b = copy.copy(lista_a)
# primeiro param é a primeira lista e o segundo é o primeiro elemento da primeira lista
lista_b[0] [0] = "batata"
print("lista A:", lista_a)
print("lista B:", lista_b)
# Como podemos ver o resultado é a alteração na lista original!
# Saída 
# lista A: [['batata', 2, 3], [4, 5, 6]]
# lista B: [['batata', 2, 3], [4, 5, 6]]