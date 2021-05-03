"""Parser for a Python assignment statements."""
import libcst

from arborista.nodes.python.assignment_statement import AssignmentStatement
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.expression import Expression
from arborista.parser import Parser
from arborista.parsers.python.assignment_targets_parser import (AssignmentTargetsParser,
                                                                LibcstAssignmentTargets)
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression

LibcstAssignmentStatement = libcst.Assign


class AssignmentStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python assignment statements."""
    @staticmethod
    def parse_assignment_statement(
            libcst_assignment_statement: LibcstAssignmentStatement) -> AssignmentStatement:
        """Parse a Python assignment statements."""
        libcst_assignment_targets: LibcstAssignmentTargets = libcst_assignment_statement.targets
        assignment_targets: AssignmentTargets = AssignmentTargetsParser.parse_assignment_targets(
            libcst_assignment_targets)

        libcst_value: LibcstExpression = libcst_assignment_statement.value
        value: Expression = ExpressionParser.parse_expression(libcst_value)

        assignment_statement: AssignmentStatement = AssignmentStatement(assignment_targets, value)

        return assignment_statement
