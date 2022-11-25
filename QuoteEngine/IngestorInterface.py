"""Abstract framework for importing files."""

from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel

from typing import List


class IngestorInterface(ABC):
    """Provide the abstract method for parsing files."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Determine if files passed are compatible."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Force inclusion of a parsing method in children classes."""
        pass
