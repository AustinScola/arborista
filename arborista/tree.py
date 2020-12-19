"""A tree structure."""
from typing import Any, Optional

from arborista.node import Node


class Tree():  # pylint: disable=too-few-public-methods
    """A tree structure."""
    def __init__(self, root: Optional[Node] = None):
        self.root: Optional[Node] = root

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Tree):
            return False

        return self.root == other.root
