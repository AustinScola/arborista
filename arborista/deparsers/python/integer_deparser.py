"""Deparser for a Python integer."""
from arborista.deparser import Deparser
from arborista.nodes.python.integer import Integer


class IntegerDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python integer."""
    @staticmethod
    def deparse_integer(integer: Integer) -> str:
        """Deparse a Python integer."""
        value: int = integer.value
        string: str = str(value)
        return string
