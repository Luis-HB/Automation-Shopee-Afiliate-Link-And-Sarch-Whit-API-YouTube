from decimal import Decimal

from models.product import Product
from models.video import Video

from services.publication.publication_payload_builder import (
    PublicationPayloadBuilder
)


produto = Product(

    id=1,

    titulo="Mouse Logitech G203",

    descricao="Mouse Gamer",

    preco=Decimal("99.90"),

    preco_original=Decimal("149.90"),

    desconto=Decimal("33.35"),

    imagem_principal="https://teste.com/img.jpg",

    url_produto="https://produto",

    url_afiliado="https://afiliado",

    score=Decimal("9.5"),

    status="PRONTO"

)

video = Video(

    id=10,

    youtube_id="abc123",

    titulo="Review Logitech G203",

    canal="Canal Tech",

    thumbnail="https://thumb.jpg",

    url="https://youtube.com/watch?v=abc123",

    views=150000,

    likes=12000,

    duracao=35,

    score=96.7

)

payload = PublicationPayloadBuilder.build(

    produto,

    video

)

from pprint import pprint

pprint(payload)