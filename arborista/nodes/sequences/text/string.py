"""A string of characters."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node


class String(Node):
    """A string of characters."""
    def __init__(self, value: str = '', parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str = value

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True
