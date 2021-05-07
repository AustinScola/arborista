"""Parser for a Python simple statement."""
from typing import Union

import libcst

from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatementList
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace
from arborista.parser import Parser
from arborista.parsers.python.small_statement_parser import (LibcstSmallStatements,
                                                             SmallStatementParser)
from arborista.parsers.python.trailing_whitespace_parser import (LibcstTrailingWhitespace,
                                                                 TrailingWhitespaceParser)

LibcstSimpleStatement = Union[libcst.SimpleStatementLine, libcst.SimpleStatementSuite]


class SimpleStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python simple statement."""
    @staticmethod
    def parse_simple_statement(libcst_simple_statement: LibcstSimpleStatement) -> SimpleStatement:
        """Parse a simple statement."""
        libcst_small_statements: LibcstSmallStatements = libcst_simple_statement.body

        small_statements: SmallStatementList = SmallStatementParser.parse_small_statements(
            libcst_small_statements)

        libcst_trailing_whitespace: LibcstTrailingWhitespace = \
            libcst_simple_statement.trailing_whitespace
        trailing_whitespace: TrailingWhitespace = \
            TrailingWhitespaceParser.parse_trailing_whitespace(libcst_trailing_whitespace)

        simple_statement: SimpleStatement = SimpleStatement(small_statements, trailing_whitespace)
        simple_statement.set_parent_in_children()

        return simple_statement
