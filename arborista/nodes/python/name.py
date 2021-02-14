"""A Python name."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.atom import Atom


class Name(Atom):
    """A Python name."""
    def __init__(self, value: str, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
