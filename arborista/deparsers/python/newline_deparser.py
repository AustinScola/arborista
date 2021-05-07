"""Deparser for a newline."""
from arborista.deparser import Deparser
from arborista.nodes.python.newline import Newline


class NewlineDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a newline."""
    @staticmethod
    def deparse_newline(newline: Newline) -> str:
        """Deparse a newline."""
        string: str = newline.value
        return string
