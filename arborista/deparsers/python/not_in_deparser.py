"""Deparser for a Python not_in."""
from arborista.deparser import Deparser
from arborista.nodes.python.not_in import NotIn


class NotInDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python not_in."""
    @staticmethod
    def deparse_not_in(not_in_: NotIn) -> str:  # pylint: disable=unused-argument
        """Deparse a Python not_in."""
        return 'not in'
