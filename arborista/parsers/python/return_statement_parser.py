"""Parser for a Python return statement."""
import libcst

from arborista.nodes.python.return_statement import ReturnStatement
from arborista.parser import Parser

LibcstReturnStatement = libcst.Return


class ReturnStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python return statement."""
    @staticmethod
    def parse_return_statement(libcst_return_statement: LibcstReturnStatement) -> ReturnStatement:  #pylint: disable=unused-argument
        """Parser a Python return statement."""
        return ReturnStatement()
