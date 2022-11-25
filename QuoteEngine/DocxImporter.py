"""Import docx files."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import docx
from typing import List


class DocxImporter(IngestorInterface):
    """Class for interpreting DOCX files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Interpret DOCX files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quote_models = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split("-")
                new_quote_model = QuoteModel(parse[0].strip('" '),
                                             parse[1].strip(' '))
                quote_models.append(new_quote_model)
        return quote_models
