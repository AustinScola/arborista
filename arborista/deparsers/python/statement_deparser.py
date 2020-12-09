"""Deparser for a Python statement."""
from typing import cast

from arborista.deparser import Deparser
from arborista.deparsers.python.compound_statement_deparser import CompoundStatementDeparser
from arborista.deparsers.python.simple_statement_deparser import SimpleStatementDeparser
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import Statement


class StatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python statement."""
    @staticmethod
    def deparse_statement(statement: Statement, indent: str) -> str:
        """Deparse a Python statement."""
        string: str
        if isinstance(statement, SimpleStatement):
            simple_statement: SimpleStatement = statement
            simple_statement_string = SimpleStatementDeparser.deparse_simple_statement(
                simple_statement, indent)
            string = simple_statement_string
        else:
            compound_statement: CompoundStatement = cast(CompoundStatement, statement)
            compound_statement_string = CompoundStatementDeparser.deparse_compound_statement(
                compound_statement, indent)
            string = compound_statement_string
        return string
