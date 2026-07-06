import time

from starlette.middleware.base import (
    BaseHTTPMiddleware,
)

from app.core.logging.logger import (
    get_logger,
)

logger = get_logger(__name__)


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        start = time.time()

        response = await call_next(
            request
        )

        duration = (
            time.time() - start
        )

        logger.info(
            "request",
            method=request.method,
            path=request.url.path,
            status=response.status_code,
            duration=round(
                duration,
                3,
            ),
        )

        return response