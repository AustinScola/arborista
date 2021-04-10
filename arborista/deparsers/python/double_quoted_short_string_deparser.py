"""Deparesr for a Python double quoted short string."""
from arborista.deparser import Deparser
from arborista.nodes.python.double_quoted_short_string import DoubleQuotedShortString


class DoubleQuotedShortStringDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparesr for a Python double quoted short string."""
    @staticmethod
    def deparse_double_quoted_short_string(
            double_quoted_short_string: DoubleQuotedShortString) -> str:
        """Return a string from a double quoted short string."""
        string: str = f'"{double_quoted_short_string.value}"'
        return string
