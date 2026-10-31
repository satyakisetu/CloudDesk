from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os

class Settings(BaseSettings):
    # App Settings
    ENVIRONMENT: str = "development"
    DEMO_MODE: bool = True
    CORS_ORIGINS: list[str] = ["*"]

    # Security
    JWT_SECRET: str = "demo-secret-change-me-in-production"
    SUPABASE_JWT_SECRET: str | None = None

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/support.db"
    CHECKPOINT_DB_PATH: str = "./data/checkpoints.db"

    # Redis
    REDIS_URL: str | None = None
    USE_FAKE_REDIS: bool = True

    # LLM
    LLM_PROVIDER: str = "fake"
    LLM_API_KEY: str | None = None
    LLM_MODEL: str = "gpt-4o" # Default for reference

    # Embedding
    EMBEDDING_PROVIDER: str = "fake"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    EMBEDDING_DIMENSIONS: int = 384

    # Vector Store
    VECTOR_STORE: str = "memory"
    QDRANT_URL: str | None = None
    QDRANT_API_KEY: str | None = None
    QDRANT_COLLECTION: str = "clouddesk_knowledge"

    # Policy & Tooling
    APPROVAL_REQUIRED_FOR_REFUNDS: bool = True
    MAX_REFUND_WITHOUT_APPROVAL: float = 0.0
    TOOL_TIMEOUT_SECONDS: int = 30
    RATE_LIMIT_PER_MINUTE: int = 120
    SAMPLE_DATA_DIR: str = "sample_data"

    # Observability
    LANGCHAIN_TRACING_V2: bool = False
    LANGCHAIN_API_KEY: str | None = None
    LANGCHAIN_PROJECT: str = "clouddesk-support"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings():
    return Settings()
