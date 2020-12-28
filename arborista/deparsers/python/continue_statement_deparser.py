"""Deparser for a Python continue statement."""
from arborista.deparser import Deparser
from arborista.nodes.python.continue_statement import ContinueStatement


class ContinueStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python continue statement."""
    @staticmethod
    def deparse_continue_statement(continue_statement: ContinueStatement) -> str:  # pylint: disable=unused-argument
        """Deparse a Python continue statement."""
        return 'continue'
