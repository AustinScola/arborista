"""A parser for a Python comparison operator."""
import libcst

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.equals import Equals
from arborista.parser import Parser
from arborista.parsers.python.equals_parser import EqualsParser, LibcstEquals

LibcstComparisonOperator = libcst.BaseCompOp


class ComparisonOperatorParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python comparison operator."""
    @staticmethod
    def parse_comparison_operator(
            libcst_comparison_operator: LibcstComparisonOperator) -> ComparisonOperator:
        """Parse a Python comparison operator."""
        comparison_operator: ComparisonOperator

        if isinstance(libcst_comparison_operator, LibcstEquals):
            libcst_equals: LibcstEquals = libcst_comparison_operator
            equals: Equals = EqualsParser.parse_equals(libcst_equals)
            comparison_operator = equals
        else:
            raise NotImplementedError  # pragma: no cover

        return comparison_operator
