"""Deparser for a Python less than."""
from arborista.deparser import Deparser
from arborista.nodes.python.less_than import LessThan


class LessThanDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python less than."""
    @staticmethod
    def deparse_less_than(less_than: LessThan) -> str:  # pylint: disable=unused-argument
        """Deparse a Python less than."""
        return '<'
