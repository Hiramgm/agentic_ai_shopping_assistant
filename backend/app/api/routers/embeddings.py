from fastapi import APIRouter

from app.core.config.settings import settings
from app.providers.embeddings import embedding_provider

router = APIRouter(
    prefix="/embeddings",
    tags=["Embeddings"]
)


@router.get("/test")
def embedding_test():

    vector = embedding_provider.embed_query(
        "gaming laptop"
    )

    return {
        "model": settings.embedding_model,
        "dimension": embedding_provider.dimension(),
        "vector_size": len(vector),
        "first_10_values": vector[:10],
    }