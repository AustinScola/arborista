"""Deparser for a Python in."""
from arborista.deparser import Deparser
from arborista.nodes.python.in_ import In


class InDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python in."""
    @staticmethod
    def deparse_in(in_: In) -> str:  # pylint: disable=unused-argument
        """Deparse a Python in."""
        return 'in'
