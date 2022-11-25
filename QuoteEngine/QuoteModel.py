"""Class for storing the author and quotation."""


class QuoteModel:
    """This class creates a model for quotation/body and author."""

    def __init__(self, quotation, author):
        """Initialize.

         This defines the author, quotation
        and body attributes of the QuoteModel class.
        """
        self.author = author
        self.quotation = quotation
        self.body = quotation

    def __repr__(self):
        """Represent this class."""
        return f'<{self.quotation}, {self.author}>'
