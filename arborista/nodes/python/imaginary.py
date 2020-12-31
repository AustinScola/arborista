"""A Python imaginary."""
from typing import Any, Optional, Union

from arborista.node import Node
from arborista.nodes.python.number import Number


class Imaginary(Number):
    """A Python imaginary."""
    def __init__(self, value: Union[int, float], parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: Union[int, float] = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Imaginary):
            return False
        return self.value == other.value
