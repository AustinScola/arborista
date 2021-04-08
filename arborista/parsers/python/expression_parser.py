"""Parser for a Python expression."""
import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.number import Number
from arborista.parser import Parser
from arborista.parsers.python.number_parser import LibcstNumber, NumberParser

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
        else:
            raise NotImplementedError  # pragma: no cover
        return expression
