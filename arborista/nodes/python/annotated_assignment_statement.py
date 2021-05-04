"""A Python annotated assignment statement."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.small_statement import SmallStatement


class AnnotatedAssignmentStatement(SmallStatement):
    """A Python annotated assignment statement."""
    def __init__(self,
                 target: Expression,
                 annotation: Expression,
                 value: Optional[Expression],
                 parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.target: Expression = target
        self.annotation: Expression = annotation
        self.value: Optional[Expression] = value
