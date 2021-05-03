"""Parser for Python assignment targets."""
from typing import List, Sequence

import libcst

from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.expression import Expression
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression

LibcstAssignmentTargets = Sequence[libcst.AssignTarget]


class AssignmentTargetsParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for Python assignment targets."""
    @staticmethod
    def parse_assignment_targets(
            libcst_assignment_targets: LibcstAssignmentTargets) -> AssignmentTargets:
        """Parse Python assignment targets."""
        libcst_first: LibcstExpression = libcst_assignment_targets[0].target
        first: Expression = ExpressionParser.parse_expression(libcst_first)

        libcst_rest = libcst_assignment_targets[1:]
        rest: List[Expression] = [
            ExpressionParser.parse_expression(libcst_target.target) for libcst_target in libcst_rest
        ]

        assignment_targets: AssignmentTargets = AssignmentTargets(first, rest)

        return assignment_targets
