"""This creates a class for storing the author and quotation for later reference."""


class QuoteModel:
    """This class creates a model for quotation/body and author."""
    def __init__(self, quotation, author):
        """The initialization method defines the author, quotation and body attributes of the QuoteModel class."""
        self.author = author
        self.quotation = quotation
        self.body = quotation

    def __repr__(self):
        """This representation method provides a helpful output."""
        return f'<{self.quotation}, {self.author}>'

