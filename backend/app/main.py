from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import (
    health,
    embeddings,
)

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

setup_logging()

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(
        "application_started",
        environment=settings.env,
    )

    yield

    logger.info("application_stopped")


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)

app.add_middleware(
    LoggingMiddleware
)

app.add_exception_handler(
    Exception,
    application_exception,
)

app.include_router(
    health.router,
    prefix="/api/v1"
)

app.include_router(
    embeddings.router,
    prefix="/api/v1"
)