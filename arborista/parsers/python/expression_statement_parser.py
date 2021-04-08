"""Parser for a Python expression statement."""
import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser

LibcstExpressionStatement = libcst.Expr


class ExpressionStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python expression statement."""
    @staticmethod
    def parse_expression_statement(
            libcst_expression_statement: LibcstExpressionStatement) -> ExpressionStatement:
        """Parse a Python expression statement."""
        libcst_expression = libcst_expression_statement.value
        expression: Expression = ExpressionParser.parse_expression(libcst_expression)

        expression_statement: ExpressionStatement = ExpressionStatement(expression)
        return expression_statement
