"""A double quoted long string."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.long_string import LongString


class DoubleQuotedLongString(LongString):
    """A double quoted long string."""
    def __init__(self, value: str, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.value: str = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value

        return equality
