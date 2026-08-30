import logging
from backend.app.security.exceptions import SecurityBlockedError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from backend.app.api.routes.search import router as search_router
from backend.app.middleware.request_id import RequestIDMiddleware

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s %(levelname)s "
        "%(name)s %(message)s"
    ),
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="GuardPay",
    description="AI-powered shopping and payment security platform",
    version="0.1.0",
)
app.add_middleware(RequestIDMiddleware)

@app.exception_handler(SecurityBlockedError)
async def security_blocked_exception_handler(
    request: Request,
    exc: SecurityBlockedError,
):
    return JSONResponse(
        status_code=403,
        content={
            "error": {
                "code": "SECURITY_BLOCKED",
                "message": exc.message,
            }
        },
    )
@app.exception_handler(Exception)
async def unexpected_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        "Unhandled exception while processing %s %s",
        request.method,
        request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "An unexpected error occurred.",
            }
        },
    )


app.include_router(search_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
