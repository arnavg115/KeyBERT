from ._base import BaseEmbedder
from ._hf_api import HfApiEmbeddingModel


def select_backend(multilingual=False, key=""):
    """Select an embedding model based on language or a specific sentence transformer models.
    When selecting a language, we choose `all-MiniLM-L6-v2` for English and
    `paraphrase-multilingual-MiniLM-L12-v2` for all other languages as it support 100+ languages.

    Returns:
        model: Either a Sentence-Transformer or Flair model
    """
    # keybert language backend

    # Flair word embeddings
    return HfApiEmbeddingModel(multilingual, key)
    # return SentenceTransformerBackend("paraphrase-multilingual-MiniLM-L12-v2")
