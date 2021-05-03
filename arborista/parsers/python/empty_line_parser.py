"""Parser for a Python empty line."""
import libcst

from arborista.nodes.python.empty_line import EmptyLine
from arborista.parser import Parser

LibcstEmptyLine = libcst.EmptyLine


class EmptyLineParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python empty line."""
    @staticmethod
    def parse_empty_line(libcst_empty_line: LibcstEmptyLine) -> EmptyLine:  # pylint: disable=unused-argument
        """Parser a Python empty line."""
        empty_line: EmptyLine = EmptyLine()
        return empty_line
