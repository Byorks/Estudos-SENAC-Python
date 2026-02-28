from dataclasses import dataclass, field
import uuid
from datetime import date

# @dataclass(frozen=True) frozen para tornar a entidade imutável
@dataclass
class Produto:
    id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
    codigo: str
    nome: str
    preco: float
    quantidade: int
    
    # __post_init__ opcional para validações extras após criação
    def __post_init__(self):
        if not self.codigo:
            raise ValueError("Código obrigatório")