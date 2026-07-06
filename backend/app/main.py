from fastapi import FastAPI

from app.core.config.settings import settings
from app.core.logging.logger import (
    setup_logging,
    get_logger,
)
from app.core.logging.middleware import (
    LoggingMiddleware,
)
from app.core.exceptions.handlers import (
    application_exception,
)

# Initialize logging
setup_logging()

logger = get_logger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name
)

# Add middleware HERE
app.add_middleware(
    LoggingMiddleware
)

# Add exception handler
app.add_exception_handler(
    Exception,
    application_exception,
)


@app.on_event("startup")
async def startup():
    logger.info(
        "application_started",
        environment=settings.env,
        llm=settings.llm_provider,
        embedding=settings.embedding_model,
    )


@app.get("/")
def root():
    logger.info("root_called")
    return {
        "message": "Agentic Shopping Assistant"
    }


@app.get("/health")
def health():
    logger.info("health_check")
    return {
        "status": "healthy",
        "environment": settings.env,
    }