from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logging.logger import (
    get_logger,
)

logger = get_logger(__name__)


async def application_exception(
    request: Request,
    exc: Exception,
):

    logger.error(
        "application_error",
        error=str(exc),
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc)
        },
    )