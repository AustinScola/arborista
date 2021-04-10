"""Deparesr for a Python single quoted short string."""
from arborista.deparser import Deparser
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString


class SingleQuotedShortStringDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparesr for a Python single quoted short string."""
    @staticmethod
    def deparse_single_quoted_short_string(
            single_quoted_short_string: SingleQuotedShortString) -> str:
        """Return a string from a double quoted short string."""
        string: str = repr(single_quoted_short_string.value)
        return string
