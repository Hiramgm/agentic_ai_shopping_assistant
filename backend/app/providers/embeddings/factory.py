from app.core.config.settings import settings
from app.core.exceptions.base import ProviderException

from app.providers.embeddings.config import (
    EmbeddingConfig,
)

from app.providers.embeddings.registry import (
    EMBEDDING_PROVIDERS,
)


class EmbeddingFactory:

    @staticmethod
    def get_provider():

        provider = settings.embedding_provider.lower()

        provider_cls = EMBEDDING_PROVIDERS.get(provider)

        if provider_cls is None:

            supported = ", ".join(
                EMBEDDING_PROVIDERS.keys()
            )

            raise ProviderException(
                f"Unsupported embedding provider '{provider}'. "
                f"Supported providers: {supported}"
            )

        config = EmbeddingConfig(
            provider=provider,
            model_name=settings.embedding_model,

            api_key=getattr(
                settings,
                f"{provider}_api_key",
                None,
            ),

            timeout=settings.embedding_timeout,

            max_retries=settings.embedding_max_retries,
        )

        return provider_cls(config)