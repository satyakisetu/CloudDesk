from fastapi import APIRouter, Depends
from backend.app.core.config import get_settings
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health/live")
async def health_live():
    """
    Liveness probe: Returns 200 if the process is running.
    No I/O checks.
    """
    return {"status": "ok", "detail": "process is alive"}

@router.get("/health/ready")
async def health_ready():
    """
    Readiness probe: Checks if critical dependencies are available.
    In v1, we check the core settings and basic availability.
    """
    # In future phases, this will check DB, Redis, Vector Store, and LLM provider.
    return {"status": "ok", "detail": "system is ready"}
