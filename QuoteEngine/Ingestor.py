"""Tie all importers together."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter
from typing import List


class Ingestor(IngestorInterface):
    """Envelope the IngestorInterface and importers."""

    allowed_extensions = ['docx', 'pdf', 'txt', 'csv']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Use the can_ingest method from the parent class IngestorInterface.

        This method also tests if extensions passed are permissible.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        ext = path.split('.')[-1]

        if ext == 'docx':
            return DocxImporter.parse(path)
        elif ext == 'csv':
            return CSVImporter.parse(path)
        elif ext == 'pdf':
            return PDFImporter.parse(path)
        else:
            return TXTImporter.parse(path)
