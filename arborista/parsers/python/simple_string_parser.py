"""Parser for a Python simple string."""
import libcst

from arborista.nodes.python.simple_string import SimpleString
from arborista.parser import Parser

LibcstSimpleString = libcst.SimpleString


class SimpleStringParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python simple string."""
    @staticmethod
    def parse_simple_string(libcst_simple_string: LibcstSimpleString) -> SimpleString:
        """Parse a Python simple string."""
        libcst_value: str = libcst_simple_string.value
        value: str = libcst_value
        simple_string: SimpleString = SimpleString(value)
        return simple_string
