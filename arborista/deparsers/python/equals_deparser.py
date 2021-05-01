"""Deparser for a Python equals."""
from arborista.deparser import Deparser
from arborista.nodes.python.equals import Equals


class EqualsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python equals."""
    @staticmethod
    def deparse_equals(equals: Equals) -> str:  # pylint: disable=unused-argument
        """Deparse a Python equals."""
        return '=='
