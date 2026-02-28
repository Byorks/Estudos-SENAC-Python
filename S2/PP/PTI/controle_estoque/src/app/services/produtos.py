
from app import limpar_console
from ..models.produto import Produto
from ..repositories.produtos import ProdutoRepository

class PessoaService: 
    # Injeção de dependência
    # Aqui estamos definindo que PessoaService espera receber um repository que seja ou herde
    # de ProdutoRepository, dessa forma evita acoplamento inserindo o ProdutoRepository
    # diretamente dentro da ProdutosServices
    def __init__(self, repo: ProdutoRepository):
     self.repo = repo





#CAMPOS = ["codigo", "nome", "preco", "quantidade"]
# # Verificado a existência do arquivo
# # Vamos fazer cadastrar novos produtos

# # montando um objeto com os campos da var CAMPOS
# # Temos que preencher o objeto com as respostas do usuário


# def cadastrar_produto():
#     # Depois precisa verificar se os campos estão sendo preenchidos corretamente

#     # verificar se cod já existe
#     # verificar se o preço ou estoque não está negativo

#     limpar_console()
#     novo_produto = {}

#     print("----> Cadastro de novo produto iniciado <----")
#     print("Insira as informações do produto")
#     novo_produto["codigo"] = input("Digite o código: ")
#     novo_produto["nome"] = input("Digite o nome: ")
#     # Precisa inserir com ponto pra dar certo
#     # adaptar para o usuário colocar virgula e funcionar
#     novo_produto["preco"] = float(input("Digite o preço: "))
#     novo_produto["qtd"] = int(input("Digite a quantidade em estoque: "))

#     # Depois de tratar os inputs

# def listar_produtos():
#     print("---- Listando produtos ----")
