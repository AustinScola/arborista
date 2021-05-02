"""A deparser for a Python index."""
from arborista.deparser import Deparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.index import Index


class IndexDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for a Python index."""
    @staticmethod
    def deparse_index(index: Index) -> str:
        """Deparse a Python index."""
        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel

        value: Expression = index.value
        string: str = ExpressionDeparser.deparse_expression(value)

        return string
