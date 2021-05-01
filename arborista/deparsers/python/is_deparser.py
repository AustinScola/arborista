"""Deparser for a Python is."""
from arborista.deparser import Deparser
from arborista.nodes.python.is_ import Is


class IsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python is."""
    @staticmethod
    def deparse_is(is_: Is) -> str:  # pylint: disable=unused-argument
        """Deparse a Python is."""
        return 'is'
