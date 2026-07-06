from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )

    app_name: str = "Agentic Shopping Assistant"
    env: str = "dev"

    llm_provider: str = "groq"
    llm_model: str = "llama-3.3-70b-versatile"

    embedding_provider: str = "local"
    embedding_model: str = "BAAI/bge-large-en-v1.5"

    vector_db: str = "pinecone"
    search_engine: str = "elasticsearch"
    graph_db: str = "neo4j"
    cache_provider: str = "redis"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()