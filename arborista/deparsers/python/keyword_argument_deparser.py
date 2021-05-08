"""Deparser for a Python keyword argument."""
from arborista.deparser import Deparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.keyword_argument import KeywordArgument
from arborista.nodes.python.name import Name


class KeywordArgumentDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python keyword argument."""
    @staticmethod
    def deparse_keyword_argument(keyword_argument: KeywordArgument) -> str:
        """Deparse a Python keyword argument."""
        string: str

        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel

        name: Name = keyword_argument.name
        name_string: str = NameDeparser.deparse_name(name)

        value: Expression = keyword_argument.value
        value_string = ExpressionDeparser.deparse_expression(value)

        string = name_string + '=' + value_string

        return string
