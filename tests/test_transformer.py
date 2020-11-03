"""Test arborista.transformer."""
import pytest

from arborista.node import Node
from arborista.transformation import Transformations
from arborista.transformer import Transformer
from arborista.tree import Tree


# yapf: disable
@pytest.mark.parametrize('transformations', [
    ([]),
])
# yapf: enable
def test_init(transformations: Transformations) -> None:
    """Test arborista.transformer.Transformer.__init__"""
    transformer: Transformer = Transformer(transformations)

    _assert_transformer_has_transformations(transformer, transformations)


def _assert_transformer_has_transformations(transformer: Transformer,
                                            transformations: Transformations) -> None:
    assert transformer.transformations == transformations


# yapf: disable
@pytest.mark.parametrize('transformations, tree', [
    ([], Tree(root=Node())),
])
# yapf: enable
def test_run(transformations: Transformations, tree: Tree) -> None:
    """Test arborista.transformer.Transformer.run"""
    transformer: Transformer = Transformer(transformations)
    with pytest.raises(NotImplementedError):
        transformer.run(tree)
