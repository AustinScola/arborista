"""Deparser for a Python less than or equals."""
from arborista.deparser import Deparser
from arborista.nodes.python.less_than_or_equals import LessThanOrEquals


class LessThanOrEqualsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python less than or equals."""
    @staticmethod
    def deparse_less_than_or_equals(less_than_or_equals: LessThanOrEquals) -> str:  # pylint: disable=unused-argument
        """Deparse a Python less than or equals."""
        return '<='
