"""A parser for a Python comparison."""
import libcst

from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.expression import Expression
from arborista.parser import Parser
from arborista.parsers.python.comparison_operator_parser import (ComparisonOperatorParser,
                                                                 LibcstComparisonOperator)

LibcstComparison = libcst.Comparison


class ComparisonParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python comparison."""
    @staticmethod
    def parse_comparison(libcst_comparison: LibcstComparison) -> Comparison:
        """Parse a Python comparison operator."""
        from arborista.parsers.python.expression_parser import (  # pylint: disable=import-outside-toplevel
            ExpressionParser, LibcstExpression)

        libcst_left: LibcstExpression = libcst_comparison.left
        left: Expression = ExpressionParser.parse_expression(libcst_left)

        if len(libcst_comparison.comparisons) > 1:
            raise NotImplementedError  # pragma: no cover

        libcst_comparison_target: libcst.ComparisonTarget = libcst_comparison.comparisons[0]

        libcst_comparison_operator: LibcstComparisonOperator = libcst_comparison_target.operator
        comparison_operator: ComparisonOperator = \
            ComparisonOperatorParser.parse_comparison_operator(libcst_comparison_operator)

        libcst_right: LibcstExpression = libcst_comparison_target.comparator
        right: Expression = ExpressionParser.parse_expression(libcst_right)

        comparison: Comparison = Comparison(left, comparison_operator, right)
        return comparison
