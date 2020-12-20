"""Assertion helper for asserting that the parent node is set in child nodes of a node."""
from typing import List

import pytest

from arborista.node import Node


def assert_parent_set_in_children(node: Node) -> None:
    """Assert that the parent node is set in child nodes of a node."""
    __tracebackhide__ = True  # pylint: disable=unused-variable

    orphans: List[Node] = [child for child in node.iterate_children() if child.parent is not node]

    if len(orphans) == 1:
        orphan = orphans[0]
        pytest.fail(f"Child node {orphan} does not have expected parent {node}.")
    elif len(orphans) > 1:
        orphans_string: str = ' '.join(map(str, orphans))
        pytest.fail(f"Child nodes {orphans_string} do not have expected parent {node}.")
