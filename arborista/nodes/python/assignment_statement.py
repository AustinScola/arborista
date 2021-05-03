"""A Python assignment statement."""

from typing import Optional

from arborista.node import Node
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.small_statement import SmallStatement


class AssignmentStatement(SmallStatement):
    """A Python assignment statement."""
    def __init__(self,
                 targets: AssignmentTargets,
                 value: Expression,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.targets: AssignmentTargets = targets
        self.value: Expression = value
