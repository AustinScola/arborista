"""A Python imaginary."""
from typing import Any, Optional, Union

from arborista.decorators.equality.equal_type import equal_type
from arborista.node import Node
from arborista.nodes.python.number import Number


class Imaginary(Number):
    """A Python imaginary."""
    def __init__(self, value: Union[int, float], parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: Union[int, float] = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
