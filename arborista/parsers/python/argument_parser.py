"""A parser for a Python argument."""
import libcst

from arborista.nodes.python.argument import Argument
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.keyword_argument import KeywordArgument
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression
from arborista.parsers.python.keyword_argument_parser import (KeywordArgumentParser,
                                                              LibcstKeywordArgument)

LibcstArgument = libcst.Arg


class ArgumentParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python argument."""
    @staticmethod
    def parse_argument(libcst_argument: LibcstArgument) -> Argument:
        """Parse a Python argument."""
        argument: Argument

        if libcst_argument.keyword:
            libcst_keyword_argument: LibcstKeywordArgument = libcst_argument
            keyword_argument: KeywordArgument = \
                KeywordArgumentParser.parse_keyword_argument(libcst_keyword_argument)
            argument = keyword_argument
        elif libcst_argument.star:
            raise NotImplementedError('Star argument parsing is not implemented yet')  # pragma: no cover  # pylint: disable=line-too-long, useless-suppression
        else:
            libcst_expression: LibcstExpression = libcst_argument.value
            expression: Expression = ExpressionParser.parse_expression(libcst_expression)
            argument = expression

        return argument
