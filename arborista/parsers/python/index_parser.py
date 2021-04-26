"""A parser for a Python index."""
import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.index import Index
from arborista.parser import Parser

LibcstIndex = libcst.Index


class IndexParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python index."""
    @staticmethod
    def parse_index(libcst_index: LibcstIndex) -> Index:
        """Parse a Python index."""
        from arborista.parsers.python.expression_parser import (  # pylint: disable=import-outside-toplevel
            ExpressionParser, LibcstExpression)

        libcst_value: LibcstExpression = libcst_index.value
        value: Expression = ExpressionParser.parse_expression(libcst_value)

        index: Index = Index(value)
        return index
