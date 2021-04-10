"""Deparesr for a Python double quoted long string."""
from arborista.deparser import Deparser
from arborista.nodes.python.double_quoted_long_string import DoubleQuotedLongString


class DoubleQuotedLongStringDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparesr for a Python double quoted long string."""
    @staticmethod
    def deparse_double_quoted_long_string(double_quoted_long_string: DoubleQuotedLongString) -> str:
        """Return a string from a double quoted long string."""
        string: str = f'"""{str(double_quoted_long_string.value)}"""'
        return string
