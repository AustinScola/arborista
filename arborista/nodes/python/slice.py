"""A Python slice."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.subscript import Subscript


class Slice(Subscript):
    """A Python slice."""
    def __init__(self,
                 start: Optional[Expression],
                 end: Optional[Expression],
                 step: Optional[Expression],
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.start: Optional[Expression] = start
        self.end: Optional[Expression] = end
        self.step: Optional[Expression] = step
