from fastapi import FastAPI
from backend.app.core.logging import setup_logging
from backend.app.middleware.request_id import RequestIdMiddleware
from backend.app.api.health import router as health_router

def create_app() -> FastAPI:
    # Initialize JSON logging
    setup_logging()

    app = FastAPI(
        title="CloudDesk Autonomous Support Platform",
        description="AI-powered support-resolution platform for CloudDesk SaaS",
        version="0.1.0"
    )

    # Middleware
    # Order: RequestId (Outermost)
    app.add_middleware(RequestIdMiddleware)

    # Routers
    app.include_router(health_router, prefix="/health", tags=["Health"])

    return app

app = create_app()
