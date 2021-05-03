"""Deparser for Python assignment targets."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.expression import Expression


class AssignmentTargetsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for Python assignment targets."""
    @staticmethod
    def deparse_assignment_targets(assignment_targets: AssignmentTargets) -> str:
        """Deparse Python assignment targets."""
        string: str

        first: Expression = assignment_targets.first
        first_string = ExpressionDeparser.deparse_expression(first)

        rest: List[Expression] = assignment_targets.rest
        rest_strings = (ExpressionDeparser.deparse_expression(assignement_target)
                        for assignement_target in rest)

        string = first_string + ''.join(', ' + assignement_target_string
                                        for assignement_target_string in rest_strings)

        return string
