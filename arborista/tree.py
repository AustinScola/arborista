"""A tree structure."""
from arborista.node import Node


class Tree():  # pylint: disable=too-few-public-methods
    """A tree structure."""
    def __init__(self, root: Node):
        self.root: Node = root
