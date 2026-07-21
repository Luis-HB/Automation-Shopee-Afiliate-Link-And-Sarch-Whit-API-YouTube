from scrapers.promobit_scraper import PromobitScraper

scraper = PromobitScraper()
contextos = scraper.execute(2)

print("=" * 80)

for ctx in contextos:
    # Trata caso o contexto seja um dicionário ou um objeto/dataclass
    if isinstance(ctx, dict):
        prod = ctx.get("product") or ctx.get("produto") or {}
        meta = ctx.get("metadata") or {}
        videos = ctx.get("videos") or []
    else:
        prod = getattr(ctx, "product", getattr(ctx, "produto", None))
        meta = getattr(ctx, "metadata", {})
        videos = getattr(ctx, "videos", [])

    # Extrai informações do produto
    if isinstance(prod, dict):
        p_id = prod.get("id")
        p_titulo = prod.get("titulo") or prod.get("title")
        p_preco = prod.get("preco") or prod.get("price")
        p_hash = prod.get("hash_produto") or prod.get("hash")
        p_imagem = prod.get("imagem_principal") or prod.get("image")
        p_shopee = prod.get("url_shopee") or prod.get("shopee_url")
        p_afiliado = prod.get("url_afiliado") or prod.get("affiliate_url")
        p_status = prod.get("status", "N/A")
    elif prod:
        p_id = getattr(prod, "id", "N/A")
        p_titulo = getattr(prod, "titulo", getattr(prod, "title", "N/A"))
        p_preco = getattr(prod, "preco", getattr(prod, "price", "N/A"))
        p_hash = getattr(prod, "hash_produto", getattr(prod, "hash", "N/A"))
        p_imagem = getattr(prod, "imagem_principal", getattr(prod, "image", "N/A"))
        p_shopee = getattr(prod, "url_shopee", getattr(prod, "shopee_url", "N/A"))
        p_afiliado = getattr(prod, "url_afiliado", getattr(prod, "affiliate_url", "N/A"))
        p_status = getattr(prod, "status", "N/A")
    else:
        p_id = p_titulo = p_preco = p_hash = p_imagem = p_shopee = p_afiliado = p_status = "N/A"

    print(f"ID: {p_id}")
    print(f"Título: {p_titulo}")
    print(f"Preço: {p_preco}")
    print(f"Hash: {p_hash}")
    print(f"Imagem: {p_imagem}")
    print(f"Shopee: {p_shopee}")
    print(f"Afiliado: {p_afiliado}")
    print(f"Status: {p_status}")
    print(f"Vídeos vinculados: {len(videos)}")
    print("=" * 80)