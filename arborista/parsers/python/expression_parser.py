"""Parser for a Python expression."""
import libcst

from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.number import Number
from arborista.nodes.python.string import String
from arborista.parser import Parser
from arborista.parsers.python.comparison_parser import ComparisonParser, LibcstComparison
from arborista.parsers.python.number_parser import LibcstNumber, NumberParser
from arborista.parsers.python.string_parser import LibcstString, StringParser

LibcstExpression = libcst.BaseExpression


class ExpressionParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python expression statement."""
    @staticmethod
    def parse_expression(libcst_expression: LibcstExpression) -> Expression:
        """Parse a Python expression statement."""
        expression: Expression
        if isinstance(libcst_expression, LibcstNumber):
            libcst_number: LibcstNumber = libcst_expression
            number: Number = NumberParser.parse_number(libcst_number)
            expression = number
        elif isinstance(libcst_expression, (libcst.SimpleString, libcst.FormattedString)):
            libcst_string: LibcstString = libcst_expression
            string: String = StringParser.parse_string(libcst_string)
            expression = string
        elif isinstance(libcst_expression, libcst.Comparison):
            libcst_comparison: LibcstComparison = libcst_expression
            comparison: Comparison = ComparisonParser.parse_comparison(libcst_comparison)
            expression = comparison
        else:
            raise NotImplementedError  # pragma: no cover
        return expression
