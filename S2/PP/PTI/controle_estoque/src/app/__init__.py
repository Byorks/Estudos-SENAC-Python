from .services.produtos import (cadastrar_produto, listar_produtos)
from .utils.console import (limpar_console, carregamento_pontos)
from .utils.arquivos import (arquivo_vazio)
from .controller.produtos import (iniciar_cadastro)
from repository.produtos import ()

"""_Centralização de funções_
Nesse caso precisei criar um project.toml definindo o empacotador backend
Porque ele não estava localizando minha pasta com o main.py
Logo após a criação instalei o pacote
pip install -e .
Instalado corretamente agora com o seguinte comando ele executa o programa sem problemas
python -m app.main
-m quer dizer que main é o script principal
"""

__all__ = [
    "cadastrar_produto", "listar_produtos",
    "limpar_console", "carregamento_pontos",
    "iniciar_cadastro"
]
