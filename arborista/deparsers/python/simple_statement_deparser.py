"""Deparser for a Python simple statement."""
from typing import Iterator

from arborista.deparser import Deparser
from arborista.deparsers.python.small_statement_deparser import SmallStatementDeparser
from arborista.nodes.python.simple_statement import SimpleStatement


class SimpleStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python simple statement."""
    @staticmethod
    def deparse_simple_statement(simple_statement: SimpleStatement, indent: str) -> str:
        """Deparse a Python simple statement."""
        small_statement_strings: Iterator[str] = (
            SmallStatementDeparser.deparse_small_statement(small_statement)
            for small_statement in simple_statement.small_statements)
        string: str = indent + '; '.join(small_statement_strings) + '\n'
        return string
