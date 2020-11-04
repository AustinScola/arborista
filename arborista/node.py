"""A node in a tree."""
from typing import Iterator, List


class Node():  # pylint: disable=too-few-public-methods
    """A node in a tree."""
    def iterate_children(self) -> Iterator['Node']:  # pylint: disable=no-self-use
        """Yield children of this node."""
        nodes: List[Node] = []
        return iter(nodes)
