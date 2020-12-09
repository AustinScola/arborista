"""Deparser for a Python return statement."""
from arborista.deparser import Deparser
from arborista.nodes.python.return_statement import ReturnStatement


class ReturnStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python return statement."""
    @staticmethod
    def deparse_return_statement(return_statement: ReturnStatement) -> str:  # pylint: disable=unused-argument
        """Deparse a Python return statement."""
        return 'return'
