"""Deparser for a Python ellipsis."""
from arborista.deparser import Deparser
from arborista.nodes.python.ellipsis_node import EllipsisNode


class EllipsisDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python ellipsis."""
    @staticmethod
    def deparse_ellipsis(ellipsis_node: EllipsisNode) -> str:  # pylint: disable=unused-argument
        """Deparse a Python ellipsis."""
        return '...'
