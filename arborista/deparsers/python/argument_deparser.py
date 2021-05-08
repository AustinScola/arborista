"""Deparser for Python argument."""
from arborista.deparser import Deparser
from arborista.deparsers.python.keyword_argument_deparser import KeywordArgumentDeparser
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.keyword_argument import KeywordArgument


class ArgumentDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for Python argument."""
    @staticmethod
    def deparse_argument(argument: Argument) -> str:
        """Deparse Python argument."""
        string: str

        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel

        if isinstance(argument, Expression):
            expression: Expression = argument
            string = ExpressionDeparser.deparse_expression(expression)
        elif isinstance(argument, KeywordArgument):
            keyword_argument: KeywordArgument = argument
            string = KeywordArgumentDeparser.deparse_keyword_argument(keyword_argument)
        else:
            raise NotImplementedError('Deparsing of argument of type {type(argument)} is not implemented yet.')  # pragma no cover  # pylint: disable=line-too-long, useless-suppression

        return string
