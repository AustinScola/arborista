"""Parser for a Python pass statement."""
import libcst

from arborista.nodes.python.pass_statement import PassStatement
from arborista.parser import Parser

LibcstPassStatement = libcst.Pass


class PassStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python pass statement."""
    @staticmethod
    def parse_pass_statement(libcst_pass_statement: LibcstPassStatement) -> PassStatement:  #pylint: disable=unused-argument
        """Parser a Python pass statement."""
        return PassStatement()
