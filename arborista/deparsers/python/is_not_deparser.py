"""Deparser for a Python is not."""
from arborista.deparser import Deparser
from arborista.nodes.python.is_not import IsNot


class IsNotDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python is not."""
    @staticmethod
    def deparse_is_not(is_not: IsNot) -> str:  # pylint: disable=unused-argument
        """Deparse a Python is not."""
        return 'is not'
