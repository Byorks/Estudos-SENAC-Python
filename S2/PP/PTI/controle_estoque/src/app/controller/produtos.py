from app import (limpar_console)
from services.produtos import (cadastrar_produto)

# Funções de cadastro - mover para controller?
def iniciar_cadastro():
    limpar_console()
    novo_produto = {}

    print("----> Cadastro de novo produto iniciado <----")
    print("Insira as informações do produto")
    novo_produto["cod"] = input("Digite o código: ")
    novo_produto["nome"] = input("Digite o nome: ")
    # Precisa inserir com ponto pra dar certo
    # adaptar para o usuário colocar virgula e funcionar
    novo_produto["preco"] = float(input("Digite o preço: "))
    novo_produto["qtd"] = int(input("Digite a quantidade em estoque: "))

    # Depois de tratar os inputs
    cadastrar_produto(**novo_produto)
