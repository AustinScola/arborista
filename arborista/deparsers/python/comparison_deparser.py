"""Deparser for a Python comparison."""
from arborista.deparser import Deparser
from arborista.deparsers.python.comparison_operator_deparser import ComparisonOperatorDeparser
from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.expression import Expression


class ComparisonDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python comparison."""
    @staticmethod
    def deparse_comparison(comparison: Comparison) -> str:
        """Deparse a Python comparison."""
        string: str

        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel

        left: Expression = comparison.left
        left_string: str = ExpressionDeparser.deparse_expression(left)

        comparison_operator: ComparisonOperator = comparison.comparison_operator
        comparison_operator_string: str = ComparisonOperatorDeparser.deparse_comparison_operator(
            comparison_operator)

        right: Expression = comparison.right
        right_string: str = ExpressionDeparser.deparse_expression(right)

        string = left_string + ' ' + comparison_operator_string + ' ' + right_string

        return string
