from fastapi import APIRouter

from app.core.config.settings import settings
from app.core.logging.logger import get_logger

router = APIRouter(
    tags=["Health"]
)

logger = get_logger(__name__)


@router.get("/")
def root():

    logger.info("root_called")

    return {
        "message": "Agentic Shopping Assistant"
    }


@router.get("/health")
def health():

    logger.info("health_check")

    return {
        "status": "healthy",
        "environment": settings.env,
        "llm": settings.llm_provider,
        "embedding": settings.embedding_model,
    }