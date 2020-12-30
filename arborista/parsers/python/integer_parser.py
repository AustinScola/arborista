"""Parser for a Python integer."""
import libcst

from arborista.nodes.python.integer import Integer
from arborista.parser import Parser

LibcstInteger = libcst.Integer


class IntegerParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python integer."""
    @staticmethod
    def parse_integer(libcst_integer: LibcstInteger) -> Integer:
        """Parser a Python integer."""
        libcst_value: str = libcst_integer.value
        value: int = int(libcst_value)
        integer: Integer = Integer(value)
        return integer
