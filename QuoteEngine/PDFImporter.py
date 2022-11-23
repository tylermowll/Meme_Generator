from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
from typing import List
import os
import random


class PDFImporter(IngestorInterface):
    """Class for interpreting PDF files."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Method for parsing PDF files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'

        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        quote_models = []

        with open(tmp, "r") as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    new_quote_model = QuoteModel(parsed[0], parsed[1])
                    quote_models.append(new_quote_model)
        os.remove(tmp)
        return quote_models
