"""A deparser for a Python expression statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.expression_statement import ExpressionStatement


class ExpressionStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for a Python expression statement."""
    @staticmethod
    def deparse_expression_statement(expression_statement: ExpressionStatement) -> str:
        """Deparse a Python expression statement."""
        expression: Expression = expression_statement.expression
        string: str = ExpressionDeparser.deparse_expression(expression)
        return string
