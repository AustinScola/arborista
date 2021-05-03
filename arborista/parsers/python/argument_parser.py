"""A parser for a Python argument."""
import libcst

from arborista.nodes.python.argument import Argument
from arborista.nodes.python.expression import Expression
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression

LibcstArgument = libcst.Arg


class ArgumentParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python argument."""
    @staticmethod
    def parse_argument(libcst_argument: LibcstArgument) -> Argument:
        """Parse a Python argument."""
        if libcst_argument.keyword:
            raise NotImplementedError('Keyword argument parsing is not implemented yet.')  # pragma: no cover  # pylint: disable=line-too-long, useless-suppression

        if libcst_argument.star:
            raise NotImplementedError('Star argument parsing is not implemented yet')  # pragma: no cover  # pylint: disable=line-too-long, useless-suppression

        libcst_expression: LibcstExpression = libcst_argument.value
        expression: Expression = ExpressionParser.parse_expression(libcst_expression)

        return expression
