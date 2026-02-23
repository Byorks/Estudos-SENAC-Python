# Código sem modularização (bloco único)
nome = "João"
nota1 = 8.0
nota2 = 7.5
nota3 = 6.0
media = (nota1 + nota2 + nota3) / 3
if media >= 7.0:
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'
print(f'Aluno:  {nome}')
print(f'Média: {media: .2f}')
print(f'Resultado: {resultado}')
# Código otimizado com funções


def calcular_media(n1, n2, n3):
    '''Calcula a média de três notas.'''
    return (n1 + n2 + n3) / 3


def verificar_aprovacao(media, media_aprovacao=7.0):
    '''Verifica se a média é suficiente para aprovação.'''
    return 'Aprovado' if media >= media_aprovacao else 'Reprovado'


def exibir_resultado(nome, media, resultado):
    '''Exibe o nome do aluno, sua média e o status de aprovação.'''
    print(f'Aluno:  {nome}')
    print(f'Média: {media: .2f}')
    print(f'Resultado: {resultado}')


# Variáveis
nome = 'João'
nota1 = 8.0
nota2 = 7.5
nota3 = 6.0
# Processamento
media = calcular_media(nota1, nota2, nota3)
resultado = verificar_aprovacao(media)
exibir_resultado(nome, media, resultado)

# Sintaxe básica de function


def nome_da_funcao(parametro1, parametro2, ):
    '''Docstring opcional explicando a função'''
    # Bloco de código da função
    return resultado

# Procedimento


def nome_do_procedimento(parametros):
    "Executa uma ação sem retornar um valor"
    # Bloco de código da função


# Definição do procedimento
def exibir_saudacao(nome):
    '''Exibe uma saudação na tela sem retornar um valor.'''
    print(f'Olá, {nome}! Seja bem-vindo!')


# Chamando o procedimento
exibir_saudacao('Lucas')
exibir_saudacao('Mariana')

'''
 Funções são ideias para calcular e retornar valores, e procedimentos para executar sem retornar algo.
 Funções tem como propósito melhorar a organização do código separando funções
 por módulos e responsabilidades.
 Outro ponto é o reaproveitamento de código evitando repetição do mesmo código sem necessidade.
 Em Python procedures sem retorno retornam por padrão o None
 '''