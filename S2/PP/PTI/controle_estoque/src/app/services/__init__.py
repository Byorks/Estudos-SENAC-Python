""" Services
Podemos deixar vazio ou com sub-centralização
Esse farei com sub-centralização para exemplo
E quando vale a pena fazer?
 - Quanto temos muitos arquivos nas subpastas e usamos as funções delas em vários lugares
"""
from .produtos import (cadastrar_produto, listar_produtos,)

__all__ = [
    "cadastrar_produto", "listar_produtos"
]