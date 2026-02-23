# Lista homogênea de números inteiros
numeros = [10, 20, 30, 40, 50]
# Acessar o terceiro elemento (índice 2)
print('Lista homogênea:', numeros)
print('Terceiro  elemento:',  numeros[2])

# Lista heterogênea com diferentes tipos de dados
dados = ['sol', 32, 2.4, 'lua', 64, True, -1.2]
# Acessar o quarto elemento (índice 3)
print('Lista heterogênea:', dados)
print('Quarto elemento:', dados[3])


import array
# Criar um array de números inteiros (‘i’ indica tipo inteiro)
numeros = array.array('i', [10, 20, 30, 40, 50])
# Exibir o array completo
print('Array:',  numeros)
# Acessar o terceiro elemento (índice 2)
print('Terceiro  elemento:',  numeros[2])

"""
Em Python é possível criar listas com conteúdos variados.
No entanto,  essa flexibilidade tem um custo, que é o desempenho e uso de memória, pois
as listas armazenam referências aos objetos em vez de valores diretos. 
Já o array apesar de sua estrutura limitada a um único tipo de dado, oferece um desempenho superior
em operações matemáticas, pos armazena os elementos de forma contígua na memória. Ou seja, próximo a memória.
Para operações numéricas mais robustas a biblioteca NumPy proporciona maior otimização e suporte a operações vetorizadas.
"""
