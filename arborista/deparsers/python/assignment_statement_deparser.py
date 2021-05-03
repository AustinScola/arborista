"""Deparser for a Python assignment statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.assignment_targets_deparser import AssignmentTargetsDeparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.nodes.python.assignment_statement import AssignmentStatement
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.expression import Expression


class AssignmentStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python assignment statement."""
    @staticmethod
    def deparse_assignment_statement(assignment_statement: AssignmentStatement) -> str:
        """Deparse a Python assignment statement."""
        string: str

        assignment_targets: AssignmentTargets = assignment_statement.targets
        assignment_targets_string = AssignmentTargetsDeparser.deparse_assignment_targets(
            assignment_targets)

        value: Expression = assignment_statement.value
        value_string = ExpressionDeparser.deparse_expression(value)

        string = assignment_targets_string + ' = ' + value_string

        return string
