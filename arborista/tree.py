"""A tree structure."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node, NodeIterator


class Tree():
    """A tree structure."""
    def __init__(self, root: Optional[Node] = None):
        self.root: Optional[Node] = root

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True

    def walk(self) -> NodeIterator:
        """Yield every node in the tree."""
        from arborista.walk import Walk  # pylint: disable=import-outside-toplevel

        walk = Walk(self)
        return walk

    def set_parents(self) -> None:
        """Set all of the parent nodes in the tree."""
        for node in self.walk():
            node.set_parent_in_children()
