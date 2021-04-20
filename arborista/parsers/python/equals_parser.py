"""A parser for a Python equals."""
import libcst

from arborista.nodes.python.equals import Equals
from arborista.parser import Parser

LibcstEquals = libcst.Equal


class EqualsParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python equals."""
    @staticmethod
    def parse_equals(libcst_equals: LibcstEquals) -> Equals:  # pylint: disable=unused-argument
        """Parse a Python equals."""
        equals: Equals = Equals()
        return equals
