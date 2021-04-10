"""Deparesr for a Python single quoted long string."""
from arborista.deparser import Deparser
from arborista.nodes.python.single_quoted_long_string import SingleQuotedLongString


class SingleQuotedLongStringDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparesr for a Python single quoted long string."""
    @staticmethod
    def deparse_single_quoted_long_string(single_quoted_long_string: SingleQuotedLongString) -> str:
        """Return a string from a single quoted long string."""
        string: str = f"'''{single_quoted_long_string.value}'''"
        return string
