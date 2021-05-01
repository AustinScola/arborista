"""Deparser for a Python not equals."""
from arborista.deparser import Deparser
from arborista.nodes.python.not_equals import NotEquals


class NotEqualsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python not equals."""
    @staticmethod
    def deparse_not_equals(not_equals: NotEquals) -> str:  # pylint: disable=unused-argument
        """Deparse a Python not equals."""
        return '!='
