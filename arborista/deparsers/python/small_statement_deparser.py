"""Deparser for a Python small statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.assignment_statement_deparser import AssignmentStatementDeparser
from arborista.deparsers.python.expression_statement_deparser import ExpressionStatementDeparser
from arborista.deparsers.python.flow_statement_deparser import FlowStatementDeparser
from arborista.deparsers.python.import_statement_deparser import ImportStatementDeparser
from arborista.deparsers.python.pass_statement_deparser import PassStatementDeparser
from arborista.nodes.python.assignment_statement import AssignmentStatement
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.small_statement import SmallStatement


class SmallStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python small statement."""
    @staticmethod
    def deparse_small_statement(small_statement: SmallStatement) -> str:
        """Deparse a Python small statement."""
        string: str
        if isinstance(small_statement, ExpressionStatement):
            expression_statement: ExpressionStatement = small_statement
            string = ExpressionStatementDeparser.deparse_expression_statement(expression_statement)
        elif isinstance(small_statement, FlowStatement):
            flow_statement: FlowStatement = small_statement
            string = FlowStatementDeparser.deparse_flow_statement(flow_statement)
        elif isinstance(small_statement, PassStatement):
            pass_statement: PassStatement = small_statement
            string = PassStatementDeparser.deparse_pass_statement(pass_statement)
        elif isinstance(small_statement, ImportStatement):
            import_statement: ImportStatement = small_statement
            string = ImportStatementDeparser.deparse_import_statement(import_statement)
        elif isinstance(small_statement, AssignmentStatement):
            assignment_statement: AssignmentStatement = small_statement
            string = AssignmentStatementDeparser.deparse_assignment_statement(assignment_statement)
        else:
            raise NotImplementedError  # pragma: no cover
        return string
