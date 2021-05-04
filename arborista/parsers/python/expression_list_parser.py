"""A parser for Python expression_list."""
from typing import List, Sequence

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.expression_list import ExpressionList
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression

LibcstExpressionList = Sequence[LibcstExpression]


class ExpressionListParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for Python expression_list."""
    @staticmethod
    def parse_expression_list(libcst_expression_list: LibcstExpressionList) -> ExpressionList:
        """Parse Python expression_list."""
        libcst_first: LibcstExpression = libcst_expression_list[0]
        first: Expression = ExpressionParser.parse_expression(libcst_first)

        libcst_rest: LibcstExpressionList = libcst_expression_list[1:]
        rest: List[Expression] = [
            ExpressionParser.parse_expression(libcst_expression)
            for libcst_expression in libcst_rest
        ]

        expression_list: ExpressionList = ExpressionList(first, rest)
        return expression_list
