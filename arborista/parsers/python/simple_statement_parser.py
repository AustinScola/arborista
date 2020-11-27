"""Parser for a Python simple statement."""
from typing import Union

import libcst

from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatementList
from arborista.parser import Parser
from arborista.parsers.python.small_statement_parser import (LibcstSmallStatements,
                                                             SmallStatementParser)

LibcstSimpleStatement = Union[libcst.SimpleStatementLine, libcst.SimpleStatementSuite]


class SimpleStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python simple statement."""
    @staticmethod
    def parse_simple_statement(libcst_simple_statement: LibcstSimpleStatement) -> SimpleStatement:
        """Parse a simple statement."""
        libcst_small_statements: LibcstSmallStatements = libcst_simple_statement.body
        small_statements: SmallStatementList = SmallStatementParser.parse_small_statements(
            libcst_small_statements)
        simple_statement: SimpleStatement = SimpleStatement(small_statements)
        return simple_statement
