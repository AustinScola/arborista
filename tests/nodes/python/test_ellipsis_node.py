"""Test arborista.nodes.python.ellipsis_node."""
from typing import Any

import pytest

from arborista.nodes.python.atom import Atom
from arborista.nodes.python.ellipsis_node import EllipsisNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.ellipsis_node.EllipsisNode inheritance."""
    assert issubclass(EllipsisNode, Atom)


# yapf: disable
@pytest.mark.parametrize('ellipsis_node, other, expected_equality', [
    (EllipsisNode(), 'foo', False),
    (EllipsisNode(), EllipsisNode(), True),
])
# yapf: enable
def test_eq(ellipsis_node: EllipsisNode, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.ellipsis_node.EllipsisNode.__eq__."""
    equality: bool = ellipsis_node == other

    assert equality == expected_equality
