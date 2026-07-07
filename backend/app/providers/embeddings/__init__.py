from app.providers.embeddings.factory import (
    EmbeddingFactory,
)

embedding_provider = (
    EmbeddingFactory.get_provider()
)