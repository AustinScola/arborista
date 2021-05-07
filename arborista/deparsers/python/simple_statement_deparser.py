"""Deparser for a Python simple statement."""
from typing import Iterator

from arborista.deparser import Deparser
from arborista.deparsers.python.small_statement_deparser import SmallStatementDeparser
from arborista.deparsers.python.trailing_whitespace_deparser import TrailingWhitespaceDeparser
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace


class SimpleStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python simple statement."""
    @staticmethod
    def deparse_simple_statement(simple_statement: SimpleStatement, indent: str) -> str:
        """Deparse a Python simple statement."""
        small_statement_strings: Iterator[str] = (
            SmallStatementDeparser.deparse_small_statement(small_statement)
            for small_statement in simple_statement.small_statements)

        trailing_whitespace: TrailingWhitespace = simple_statement.trailing_whitespace
        trailing_whitespace_string: str = \
            TrailingWhitespaceDeparser.deparse_trailing_whitespace(trailing_whitespace)

        string: str = indent + '; '.join(small_statement_strings) + trailing_whitespace_string

        return string
