
## *args quando você não sabe quantos argumentos serão passados
# Dessa forma a função receberá uma tupla como argumento
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

## Dentro da função args vai se tornar uma tupla acessível 
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

# Saída
# Type: <class 'tuple'>
# First argument: Emil
# Second argument: Tobias
# All arguments: ('Emil', 'Tobias', 'Linus')

# É possível combinar argumentos comuns com *args
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#Exemplo prático
def minha_funcao(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(minha_funcao(1,2,3))
print(minha_funcao(10, 20, 30, 40))
print(minha_funcao(5))


## ----- **kwargs ----

"""
Quando você não sabe quantas chaves serão passadas como argumentos usar **
permite adicionar dicionários como argumentos
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

## **kwargs vai permitir receber quantos argumentos forem necessários como chaves
# dentro da função o **kwargs vai se tornar um dicionário acessível
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

## Também é possível usar ele com argumentos comuns
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

## Combinando *args e **kwargs
# Deve obedecer a seguinte ordem
# 1 - Parâmetros regulares
# 2 - *args
# 3 - **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

## Desempacotando argumentos 
# Os operadores * e ** também podem ser utilizados quando chamados em funções 
# para desempacotar/expandir uma lista ou dicionário

# Se tem uma lista com items utilizar * para separar em argumentos individuais
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

## Se tem keywords/palavras-chave em um dicionário, podemos utilizar **
def minha_funcao_nome(nome, sobrenome):
  print(f"Olá, {nome} {sobrenome}!")
  
# Lembrando que as chaves precisam ter o mesmo nome que os argumentos da funçao
pessoinha = {
  "nome": "Vanessa Byork",
  "sobrenome": "Ferreira"
}

minha_funcao_nome(**pessoinha)
