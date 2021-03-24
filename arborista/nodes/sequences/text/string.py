"""A string of characters."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.standard_equality import standard_equality

from arborista.node import Node


class String(Node):
    """A string of characters."""
    def __init__(self, value: str = '', parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str = value

    @standard_equality
    def __eq__(self, other: Any) -> bool:
        pass  # pragma: no cover
