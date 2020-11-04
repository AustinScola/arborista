"""Test arborista.node."""
from typing import Iterator

from arborista.node import Node


def test_node_iterate_children() -> None:
    """Test arborista.node.iterate_children."""
    node: Node = Node()
    children_iterator: Iterator[Node] = node.iterate_children()
    assert list(children_iterator) == []
