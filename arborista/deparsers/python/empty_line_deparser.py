"""Deparser for a Python empty line."""
from arborista.deparser import Deparser
from arborista.nodes.python.empty_line import EmptyLine


class EmptyLineDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python empty line."""
    @staticmethod
    def deparse_empty_line(star: EmptyLine) -> str:  # pylint: disable=unused-argument
        """Deparse a Python empty line."""
        return '\n'
