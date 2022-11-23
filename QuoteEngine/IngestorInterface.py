from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel

from typing import List


class IngestorInterface(ABC):
    """Provide the abstract method for parsing files and determining if the files are compatible."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Method for determining if files passed are compatible."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method for forcing inclusion of a parsing method in children classes."""
        pass
