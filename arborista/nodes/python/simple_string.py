"""A Python simple string."""
from typing import Any, Iterable, List, Optional

from arborista.decorators.equality.equal_type import equal_type
from arborista.node import Node
from arborista.nodes.python.string import String


class SimpleString(String):
    """A Python simple string."""
    def __init__(self, value: Optional[str] = '', parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str
        if value is None:
            self.value = ''
        else:
            self.value = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if not self.value == other.value:
            return False

        return True


SimpleStrings = Iterable[SimpleString]
SimpleStringList = List[SimpleString]
