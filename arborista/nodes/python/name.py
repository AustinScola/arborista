"""A Python name."""
from typing import Iterable, Optional

from arborista.node import Node
from arborista.nodes.python.atom import Atom


class Name(Atom):
    """A Python name."""
    def __init__(self, value: str, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str = value


Names = Iterable[Name]
