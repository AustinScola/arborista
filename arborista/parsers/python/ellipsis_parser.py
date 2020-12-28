"""Parser for a Python ellipsis."""
import libcst

from arborista.nodes.python.ellipsis_node import EllipsisNode
from arborista.parser import Parser

LibcstEllipsis = libcst.Ellipsis


class EllipsisParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python ellipsis."""
    @staticmethod
    def parse_ellipsis(libcst_ellipsis: LibcstEllipsis) -> EllipsisNode:  # pylint: disable=unused-argument
        """Parser a Python ellipsis."""
        ellipsis: EllipsisNode = EllipsisNode()
        return ellipsis
