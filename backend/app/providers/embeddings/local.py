# from typing import List

# from sentence_transformers import (
#     SentenceTransformer,
# )

# from app.providers.embeddings.base import (
#     BaseEmbedding,
# )

# from app.core.logging.logger import (
#     get_logger
# )

# logger = get_logger(__name__)


# class LocalEmbedding(
#     BaseEmbedding
# ):

#     def __init__(
#         self,
#         model_name: str,
#     ):
#         self.model = SentenceTransformer(
#             model_name
#         )
#         logger.info(
#             "embedding_model_loaded",
#             model_name=model_name,
#         )

#     def embed_query(
#         self,
#         text: str,
#     ) -> List[float]:

#         return self.model.encode(
#             text,
#             normalize_embeddings=True,
#         ).tolist()

#     def embed_documents(
#         self,
#         texts: List[str],
#     ) -> List[List[float]]:

#         return self.model.encode(
#             texts,
#             normalize_embeddings=True,
#         ).tolist()

#     def dimension(self) -> int:
#         dimension = self.model.get_sentence_embedding_dimension()

#         if dimension is None:
#             raise ValueError("Embedding model did not report a dimension.")

#         return dimension