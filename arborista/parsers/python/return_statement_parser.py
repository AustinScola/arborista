"""Parser for a Python return statement."""
from typing import Optional

import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression

LibcstReturnStatement = libcst.Return


class ReturnStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python return statement."""
    @staticmethod
    def parse_return_statement(libcst_return_statement: LibcstReturnStatement) -> ReturnStatement:
        """Parser a Python return statement."""
        libcst_value: Optional[LibcstExpression] = libcst_return_statement.value
        value: Optional[Expression]
        if libcst_value is None:
            value = None
        else:
            value = ExpressionParser.parse_expression(libcst_value)

        return_statement: ReturnStatement = ReturnStatement(value)

        return return_statement
