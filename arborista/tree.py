"""A tree structure."""
from typing import Optional

from arborista.node import Node


class Tree():  # pylint: disable=too-few-public-methods
    """A tree structure."""
    def __init__(self, root: Optional[Node] = None):
        self.root: Optional[Node] = root
