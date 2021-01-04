"""Test arborista.transformation."""
import pytest

from arborista.node import Node
from arborista.transformation import Transformation
from testing_helpers.animal_nodes import Dog


def test_node_types() -> None:
    """Test arborista.transformation.Transformation.NODE_TYPES."""
    assert Transformation.NODE_TYPES == set()


# yapf: disable
@pytest.mark.parametrize('node', [
    (Dog())
])
# yapf: enable
def test_maybe_transform(node: Node) -> None:
    """Test arborista.transformation.Transformation.maybe_transform."""
    with pytest.raises(NotImplementedError):
        Transformation.maybe_transform(node)
