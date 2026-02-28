import csv
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
from app import arquivo_vazio
from ..models.produto import Produto

CAMPOS = ["codigo", "nome", "preco", "quantidade"]
CSV_FILE = Path("../data/produtos.csv")


class ProdutoRepository:
    def __init__(self):
        self._verificar_arquivo()
    
    def _verificar_arquivo():
        if not CSV_FILE.exists():
            # Cria pasta data se nào existir
            CSV_FILE.parent.mkdir(parents=True, exist_ok=True)
            with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)  # Cria escritor CSV
                # Seria possível assim: nova_lista = ["id", *CAMPOS] com uso de args
                writer.writerow(CAMPOS)
      
                
    # A seta é pra mostrar o tipo que vai ser retornado 
    # Type hint
    def _ler_todos(self) -> List[Dict]:
        if arquivo_vazio():
            return[]
        with CSV_FILE.open("r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)