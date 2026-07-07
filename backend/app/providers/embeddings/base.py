from abc import ABC, abstractmethod
from typing import List

from app.providers.embeddings.config import EmbeddingConfig


class BaseEmbedding(ABC):
    def __init__(self, config: EmbeddingConfig):
        self.config = config

    @abstractmethod
    def embed_query(self, text: str) -> List[float]:
        """Embed a single query."""
        raise NotImplementedError

    @abstractmethod
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple documents."""
        raise NotImplementedError

    @abstractmethod
    def dimension(self) -> int:
        """Return embedding vector dimension."""
        raise NotImplementedError