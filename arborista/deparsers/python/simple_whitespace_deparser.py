"""Deparser for a simple whitespace."""
from arborista.deparser import Deparser
from arborista.nodes.python.simple_whitespace import SimpleWhitespace


class SimpleWhitespaceDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a simple whitespace."""
    @staticmethod
    def deparse_simple_whitespace(simple_whitespace: SimpleWhitespace) -> str:
        """Deparse a simple whitespace."""
        string: str = simple_whitespace.value
        return string
