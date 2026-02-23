"""
O escopo da variável fica restrita a função, ou seja ao seu bloco de execução
Mas a função tem acesso a variáveis de escopo global
"""

# Definição de uma variável global
mensagem_global = "Olá, bem-vindo ao programa!"
def saudacao(nome):
    """Função que usa uma variável global e uma variável local."""
    mensagem_local = f'Olá, {nome}! Tenha um ótimo dia!'
\
# Variável local
print(mensagem_global)  # Acessando a variável global
print(mensagem_local)  # Acessando a variável local # Isso resultaria em um erro pois a variável é local
# Chamando a função
saudacao('Lucas')

# Variáveis locais são aquelas definidas dentro de funções, seu escopo fica limitado a mesma
# Variáveis globais podem ser acessadas por funções
# O tutor indica o uso de variáveis locais para evitar dificuldade para encontrar onde erros podem se encontrar
