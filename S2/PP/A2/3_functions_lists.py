"""
Listas passadas como argumentos são referências, portanto, não é passado uma cópia, 
é como se apontasse para a original.
Então modificar uma lista através de funções vai modificar a lista originalmente criada.
"""

def adicionar_elemento(lista):
    lista.append(100) # Modifica a lista original

numeros = [ 10, 20, 30]
adicionar_elemento(numeros)
print("Lista após a função: ", numeros)

"""
É possível copiar uma lista para evitar que uma lista seja modificada por referência
"""
def adicionar_elemento_sem_modificar(lista):
    nova_lista = lista.copy()	# Cria uma cópia
    nova_lista.append(100)
    return nova_lista	# Retorna a lista modificada sem alterar a original
numeros = [10, 20, 30]
nova_lista  =  adicionar_elemento_sem_modificar(numeros)
print('Lista original:', numeros)
print('Nova lista modificada:', nova_lista)
