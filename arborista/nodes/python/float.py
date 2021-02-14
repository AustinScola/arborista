"""A Python float."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.number import Number


class Float(Number):
    """A Python float."""
    def __init__(self, value: float, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: float = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
