"""A relative dotted name."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.python_node import PythonNode


class RelativeDottedName(PythonNode):
    """A relative dotted name."""
    def __init__(self, dots: int, dotted_name: Optional[DottedName], parent: Optional[Node] = None):
        super().__init__(parent)

        self.dots: int = dots
        self.dotted_name: Optional[DottedName] = dotted_name

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.dots != other.dots:
            return False

        if self.dotted_name != other.dotted_name:
            return False

        return True
