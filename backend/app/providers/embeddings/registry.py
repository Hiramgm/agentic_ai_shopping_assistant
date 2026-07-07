from app.providers.embeddings.jina import JinaEmbedding
# from app.providers.embeddings.openai import OpenAIEmbedding
# from app.providers.embeddings.voyage import VoyageEmbedding
# from app.providers.embeddings.local import LocalEmbedding

EMBEDDING_PROVIDERS = {
    "jina": JinaEmbedding,
    # "openai": OpenAIEmbedding,
    # "voyage": VoyageEmbedding,
    # "local": LocalEmbedding,
}