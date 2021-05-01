"""Deparser for a Python less than or than."""
from arborista.deparser import Deparser
from arborista.nodes.python.less_greater_than import LessGreaterThan


class LessGreaterThanDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python less than or than."""
    @staticmethod
    def deparse_less_greater_than(less_greater_than: LessGreaterThan) -> str:  # pylint: disable=unused-argument
        """Deparse a Python less than or than."""
        return '<>'
