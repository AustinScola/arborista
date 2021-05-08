"""A Parser for keyword arguments."""
from typing import Optional

import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.keyword_argument import KeywordArgument
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression
from arborista.parsers.python.name_parser import LibcstName, NameParser

LibcstKeywordArgument = libcst.Arg


class KeywordArgumentParser(Parser):  # pylint: disable=too-few-public-methods
    """A Parser for keyword arguments."""
    @staticmethod
    def parse_keyword_argument(libcst_keyword_argument: LibcstKeywordArgument) -> KeywordArgument:
        """Parser a keyword argument."""
        keyword_argument: KeywordArgument

        libcst_name: Optional[LibcstName] = libcst_keyword_argument.keyword
        name: Name
        if libcst_name is None:
            raise ValueError('Expected keyword argument to have a name.')  # pragma: no cover
        name = NameParser.parse_name(libcst_name)

        libcst_value: LibcstExpression = libcst_keyword_argument.value
        value: Expression = ExpressionParser.parse_expression(libcst_value)

        keyword_argument = KeywordArgument(name, value)

        return keyword_argument
