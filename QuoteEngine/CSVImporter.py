"""Importer for csv files."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd
from typing import List


class CSVImporter(IngestorInterface):
    """Class for interpreting CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse CSV files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quote_models = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            if row['body'] != "":
                new_quote_model = QuoteModel(row['body'], row['author'])
                quote_models.append(new_quote_model)
        return quote_models
