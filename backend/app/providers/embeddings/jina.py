from typing import List

import httpx

from app.core.exceptions.base import ProviderException
from app.core.logging.logger import get_logger

from app.providers.embeddings.base import BaseEmbedding
from app.providers.embeddings.config import EmbeddingConfig

logger = get_logger(__name__)


class JinaEmbedding(BaseEmbedding):

    BASE_URL = "https://api.jina.ai/v1/embeddings"

    def __init__(self, config: EmbeddingConfig):
        super().__init__(config)

        if not config.api_key:
            raise ProviderException(
                "JINA_API_KEY is missing."
            )

        self.headers = {
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json",
        }

        logger.info(
            "embedding_provider_initialized",
            provider="jina",
            model=config.model_name,
        )

    def _embed(self, input_data: List[str]) -> List[List[float]]:
        payload = {
            "model": self.config.model_name,
            "input": input_data,
        }

        try:
            response = httpx.post(
                self.BASE_URL,
                headers=self.headers,
                json=payload,
                timeout=self.config.timeout,
            )

            response.raise_for_status()

            result = response.json()

            return [
                item["embedding"]
                for item in result["data"]
            ]

        except httpx.HTTPError as exc:
            raise ProviderException(
                f"Jina embedding request failed: {exc}"
            ) from exc

    def embed_query(self, text: str) -> List[float]:
        return self._embed([text])[0]

    def embed_documents(
        self,
        texts: List[str],
    ) -> List[List[float]]:
        return self._embed(texts)

    def dimension(self) -> int:
        """
        Jina v3 embeddings are 1024-dimensional.
        """
        return 1024