"""A Python simple string."""
from typing import Any, Iterable, List, Optional

from arborista.node import Node
from arborista.nodes.python.string import String


class SimpleString(String):
    """A Python simple string."""
    def __init__(self, value: str, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SimpleString):
            return False

        if not self.value == other.value:
            return False

        return True


SimpleStrings = Iterable[SimpleString]
SimpleStringList = List[SimpleString]
