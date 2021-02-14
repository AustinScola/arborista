"""A tree structure."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node, NodeIterator


class Tree():
    """A tree structure."""
    def __init__(self, root: Optional[Node] = None):
        self.root: Optional[Node] = root

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.root == other.root
        return equality

    def walk(self) -> NodeIterator:
        """Yield every node in the tree."""
        from arborista.walk import Walk  # pylint: disable=import-outside-toplevel

        walk = Walk(self)
        return walk

    def set_parents(self) -> None:
        """Set all of the parent nodes in the tree."""
        for node in self.walk():
            node.set_parent_in_children()
