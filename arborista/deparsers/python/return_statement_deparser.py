"""Deparser for a Python return statement."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.return_statement import ReturnStatement


class ReturnStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python return statement."""
    @staticmethod
    def deparse_return_statement(return_statement: ReturnStatement) -> str:
        """Deparse a Python return statement."""
        string: str

        value: Optional[Expression] = return_statement.value
        if value is not None:
            value_string: str = ExpressionDeparser.deparse_expression(value)
            string = 'return ' + value_string
        else:
            string = 'return'

        return string
