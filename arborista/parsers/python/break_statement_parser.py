"""Parser for a Python break statement."""
import libcst

from arborista.nodes.python.break_statement import BreakStatement
from arborista.parser import Parser

LibcstBreakStatement = libcst.Break


class BreakStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python break statement."""
    @staticmethod
    def parse_break_statement(libcst_break_statement: LibcstBreakStatement) -> BreakStatement:  #pylint: disable=unused-argument
        """Parser a Python break statement."""
        return BreakStatement()
