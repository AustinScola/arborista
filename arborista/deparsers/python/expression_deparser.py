"""A deparser for a Python expression."""
from arborista.deparser import Deparser
from arborista.deparsers.python.string_deparser import StringDeparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.string import String


class ExpressionDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for a Python expression."""
    @staticmethod
    def deparse_expression(expression: Expression) -> str:
        """Deparse a Python expression."""
        string: str

        if isinstance(expression, String):
            string_node = expression
            string = StringDeparser.deparse_string(string_node)
        else:
            raise NotImplementedError  # pragma: no cover

        return string
