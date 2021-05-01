"""Deparser for a Python greater than."""
from arborista.deparser import Deparser
from arborista.nodes.python.greater_than import GreaterThan


class GreaterThanDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python greater than."""
    @staticmethod
    def deparse_greater_than(greater_than: GreaterThan) -> str:  # pylint: disable=unused-argument
        """Deparse a Python greater than."""
        return '>'
