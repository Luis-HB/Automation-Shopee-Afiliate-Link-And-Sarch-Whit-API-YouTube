from pipelines.affiliate_pipeline import AffiliatePipeline

pipeline = AffiliatePipeline()

resultado = pipeline.executar(

    keyword="mouse",

    paginas=2,

    limite=10

)

print(resultado["estatisticas"])