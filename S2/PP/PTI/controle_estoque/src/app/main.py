# Agora os imports funcionam
from .utils.console import carregamento_pontos, limpar_console
from .services.produtos import ProdutoService
from .repositories.produtos import ProdutoRepository
from .utils.console import limpar_console

# MVP
""" Cadastrar Produto
    Permitir o cadastro de um novo produto no 
    estoque, solicitando ao usuário as informações necessárias. O 
    sistema não deve permitir o cadastro de produtos com código 
    duplicado e deve validar os dados informados, garantindo que 
    o preço e a quantidade não sejam negativos. 
"""
""" Calcular o Total de Produtos em Estoque
    Calcular e exibir a 
    quantidade total de produtos armazenados no estoque, 
    considerando a soma das quantidades de todos os produtos 
    cadastrados. 
"""

""" To-do
Fazer função de carregamento visual com pontos
Menu ser selecionável via teclado setas para mover e espaço para confirmar

 --- Listagem
 Listar por ordem.... tipo por nome, por preço, etc
 
"""

repo = ProdutoRepository()
service = ProdutoService(repo)

menu_ativo = True
res_usuario = ''
# Funções de cadastro - mover para controller?


def iniciar_cadastro():
    limpar_console()

    produto = {}

    print("----> Cadastro de novo produto iniciado <----")
    print("Insira as informações do produto")
    produto["codigo"] = input("Digite o código: ")
    produto["nome"] = input("Digite o nome: ")
    # Precisa inserir com ponto pra dar certo
    # adaptar para o usuário colocar virgula e funcionar
    produto["preco"] = float(input("Digite o preço: "))
    produto["quantidade"] = int(input("Digite a quantidade em estoque: "))

    # Depois de tratar os inputs
    service.cadastrar(**produto)


def menu(menu_ativo):
    # To-do legal -> Ser selecionável via teclado setas para mover e espaço para confirmar
    # Colocar comando para fechar o menu
    while (menu_ativo):
        print("------ Menu de acesso ------")
        # Ao ver produtos temos que ter uma funcionalidade de calcular quantos prods tem em estoque
        print("- Ver produtos [1]")
        print("- Cadastrar produtos [2]")
        print("- Fechar menu digite -> Fechar\n")

        res_usuario = input("Digite a opção desejada: ")

        print(res_usuario)

        match res_usuario.lower():
            case "fechar":
                menu_ativo = False
                carregamento_pontos()
                print("Menu encerrado")

                break
            case "1":
                print("Aqui vai ficar a listagem de prods")
            case "2":
                iniciar_cadastro()
            case _:
                limpar_console()
                print("Digite uma opção valida\n")


menu(menu_ativo)
