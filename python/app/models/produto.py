from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from datetime import datetime

@dataclass
class Produto:

    id: Optional[int]=None
    descoberta_id: Optional[int]=None

    shopee_id: Optional[str]=None

    hash_produto: str=""

    titulo: str=""

    descricao: Optional[str]=None

    categoria_id: Optional[int]=None

    preco: Optional[Decimal]=None

    preco_original: Optional[Decimal]=None

    desconto: Optional[Decimal]=None

    nota: Optional[Decimal]=None

    avaliacoes: Optional[int]=None

    vendas: Optional[int]=None

    estoque: Optional[int]=None

    imagem_principal: str=""

    url_produto: str=""

    url_afiliado: str=""

    score: Decimal=Decimal("0")

    status: str="NOVO"

    ativo: bool=True

    ultima_verificacao: Optional[datetime] = None

    api_response: Optional[dict] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data):
        obj = cls()

        for field in cls.__dataclass_fields__.keys():
            if field in data:
                setattr(obj, field, data[field])

        return obj