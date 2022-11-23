from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTImporter(IngestorInterface):
    """Class for interpreting TXT files."""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Method for parsing TXT files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quote_models = []

        with open(path, encoding='utf-8-sig') as text:
            for line in text:
                if line != "":
                    new_quote_model = QuoteModel(line.split('-')[0].strip(' \n'), line.split('-')[1].strip(' \n'))
                    quote_models.append(new_quote_model)
        return quote_models


