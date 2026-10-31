from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid
import logging

logger = logging.getLogger(__name__)

class RequestIdMiddleware(BaseHTTPMiddleware):
    """
    Middleware to ensure every request has a unique X-Request-ID.
    If provided by the client, it uses it; otherwise, it generates a new UUID.
    """
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID")
        if not request_id:
            request_id = str(uuid.uuid4())

        # Store request_id in request state for access in routes and logging
        request.state.request_id = request_id

        response = await call_next(request)

        # Return the request ID in the response header
        response.headers["X-Request-ID"] = request_id
        return response
