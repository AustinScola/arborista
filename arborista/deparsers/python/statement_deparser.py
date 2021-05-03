"""Deparser for a Python statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.compound_statement_deparser import CompoundStatementDeparser
from arborista.deparsers.python.empty_line_deparser import EmptyLineDeparser
from arborista.deparsers.python.simple_statement_deparser import SimpleStatementDeparser
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.empty_line import EmptyLine
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import Statement


class StatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python statement."""
    @staticmethod
    def deparse_statement(statement: Statement, indent: str) -> str:
        """Deparse a Python statement."""
        string: str

        if isinstance(statement, EmptyLine):
            empty_line: EmptyLine = statement
            empty_line_string = EmptyLineDeparser.deparse_empty_line(empty_line)
            string = empty_line_string
        elif isinstance(statement, SimpleStatement):
            simple_statement: SimpleStatement = statement
            simple_statement_string = SimpleStatementDeparser.deparse_simple_statement(
                simple_statement, indent)
            string = simple_statement_string
        elif isinstance(statement, CompoundStatement):
            compound_statement: CompoundStatement = statement
            compound_statement_string = CompoundStatementDeparser.deparse_compound_statement(
                compound_statement, indent)
            string = compound_statement_string
        else:
            raise NotImplementedError  # pragma: no cover

        return string
