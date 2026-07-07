from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class EmbeddingConfig:
    """
    Configuration shared by all embedding providers.
    """

    provider: str
    model_name: str

    api_key: Optional[str] = None

    api_base: Optional[str] = None

    timeout: int = 60

    max_retries: int = 3