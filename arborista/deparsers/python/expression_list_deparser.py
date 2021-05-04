"""Deparser for Python expression lists."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.expression_list import ExpressionList


class ExpressionListDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for Python expression lists."""
    @staticmethod
    def deparse_expression_list(expression_list: ExpressionList) -> str:
        """Deparse Python expression lists."""
        string: str

        first: Expression = expression_list.first
        first_string = ExpressionDeparser.deparse_expression(first)

        rest: List[Expression] = expression_list.rest
        rest_strings = (ExpressionDeparser.deparse_expression(expression) for expression in rest)

        string = first_string + ''.join(', ' + expression_string
                                        for expression_string in rest_strings)

        return string
