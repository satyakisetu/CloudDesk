import logging
import json
import sys
from datetime import datetime, timezone
from typing import Any
from backend.app.core.config import get_settings

class JsonFormatter(logging.Formatter):
    """
    Custom formatter to output logs in JSON format.
    Includes request_id and workflow_id if present in the extra record.
    """
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "timestamp": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "file": record.filename,
            "line": record.lineno,
        }

        # Include extra fields passed via logging.info(..., extra={})
        if hasattr(record, "request_id"):
            log_record["request_id"] = record.request_id
        if hasattr(record, "workflow_id"):
            log_record["workflow_id"] = record.workflow_id

        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_record)

def setup_logging():
    """
    Configures the application to use JSON logging to stdout.
    """
    settings = get_settings()

    # Root logger configuration
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO if settings.ENVIRONMENT == "production" else logging.DEBUG)

    # Clear existing handlers to avoid duplicate logs
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    root_logger.addHandler(handler)

    logging.info("Logging initialized in JSON format", extra={"environment": settings.ENVIRONMENT})
