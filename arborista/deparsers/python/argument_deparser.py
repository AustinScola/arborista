"""Deparser for Python argument."""
from arborista.deparser import Deparser
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.expression import Expression


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
        else:
            raise NotImplementedError  # pragma no cover
        return string
