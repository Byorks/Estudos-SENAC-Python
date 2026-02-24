# Concatenando strings

s1 = 'Olá'
s2 = 'Mundo'
resultado = s1 + ' ' + s2
print(resultado)	# Saída: Olá Mundo

# Repete n vezes a string indicada
s = 'Python '
print(s  *  3)	# Saída: Python Python Python

# Conta quantos caracteres tem em uma string
s = 'Python'
print(len(s))	# Saída: 6

# Acessando caracteres em uma string
s = 'Python'
print(s[0]) # Saída: P  (primeiro  caractere)
print(s[-1]) # Saída: n (último caractere)

# Seguindo essa premissa de verificar o ultimo carácter, podemos inverter uma palavra
s ='Python'
print(s[::-1])	# Saída: nohtyP


# É possível verificar se uma substring está contida em uma string da nossa escolha
s = 'Python é incrível'
print('Python'  in  s)	# True
print('Java' not in s) # True
