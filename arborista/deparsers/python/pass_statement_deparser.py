"""Deparser for a Python pass statement."""
from arborista.deparser import Deparser
from arborista.nodes.python.pass_statement import PassStatement


class PassStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python pass statement."""
    @staticmethod
    def deparse_pass_statement(pass_statement: PassStatement) -> str:  # pylint: disable=unused-argument
        """Deparse a Python pass statement."""
        return 'pass'
