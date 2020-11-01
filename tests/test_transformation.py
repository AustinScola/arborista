"""Test arborista.transformation."""
import pytest

from arborista.node import Node
from arborista.transformation import Transformation


# yapf: disable
@pytest.mark.parametrize('node', [
    (Node())
])
# yapf: enable
def test_maybe_transform(node: Node):
    """Test arborista.transformation.Transformation.maybe_transform."""
    with pytest.raises(NotImplementedError):
        Transformation.maybe_transform(node)
