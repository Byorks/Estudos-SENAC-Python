from dataclasses import dataclass, field
import uuid
from datetime import date

# @dataclass(frozen=True) frozen para tornar a entidade imutável
@dataclass (frozen=True) # Não permite alterações na entidade
class Produto:
    id: uuid.UUID = field(default_factory=uuid.uuid4, init=False) # o init=False diz que ao criar um prod ele não precisa passar o argumento id
    codigo: str
    nome: str
    preco: float
    quantidade: int
    
    # __post_init__ opcional para validações extras após criação
    def __post_init__(self):
        if not self.codigo:
            raise ValueError("Código obrigatório")