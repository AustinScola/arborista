"""Deparser for a Python greater than or equals."""
from arborista.deparser import Deparser
from arborista.nodes.python.greater_than_or_equals import GreaterThanOrEquals


class GreaterThanOrEqualsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python greater than or equals."""
    @staticmethod
    def deparse_greater_than_or_equals(greater_than_or_equals: GreaterThanOrEquals) -> str:  # pylint: disable=unused-argument
        """Deparse a Python greater than or equals."""
        return '>='
