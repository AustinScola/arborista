"""Deparser for a Python break statement."""
from arborista.deparser import Deparser
from arborista.nodes.python.break_statement import BreakStatement


class BreakStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python break statement."""
    @staticmethod
    def deparse_break_statement(break_statement: BreakStatement) -> str:  # pylint: disable=unused-argument
        """Deparse a Python break statement."""
        return 'break'
