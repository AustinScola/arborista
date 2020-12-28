"""Parser for a Python continue statement."""
import libcst

from arborista.nodes.python.continue_statement import ContinueStatement
from arborista.parser import Parser

LibcstContinueStatement = libcst.Continue


class ContinueStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python continue statement."""
    @staticmethod
    def parse_continue_statement(
        libcst_continue_statement: LibcstContinueStatement  # pylint: disable=unused-argument
    ) -> ContinueStatement:
        """Parser a Python continue statement."""
        return ContinueStatement()
