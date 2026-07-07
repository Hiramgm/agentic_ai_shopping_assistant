from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[4]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Agentic Shopping Assistant"
    env: str = "dev"

    llm_provider: str = "groq"
    llm_model: str = "llama-3.3-70b-versatile"

    embedding_provider: str = "local"
    embedding_model: str = "BAAI/bge-large-en-v1.5"
    jina_api_key: str = ""

    embedding_timeout: int = 60
    embedding_max_retries: int = 3

    vector_db: str = "pinecone"
    search_engine: str = "elasticsearch"
    graph_db: str = "neo4j"
    cache_provider: str = "redis"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
