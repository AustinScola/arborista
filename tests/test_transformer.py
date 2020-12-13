"""Test arborista.transformer."""
import pytest

from arborista.node import Node
from arborista.transformation import Transformations, TransformationSet
from arborista.transformer import Transformer
from arborista.tree import Tree


# yapf: disable
@pytest.mark.parametrize('transformations, expected_transformations', [
    ([], set()),
])
# yapf: enable
def test_init(transformations: Transformations,
              expected_transformations: TransformationSet) -> None:
    """Test arborista.transformer.Transformer.__init__"""
    transformer: Transformer = Transformer(transformations)

    _assert_transformer_has_transformations(transformer, expected_transformations)


def _assert_transformer_has_transformations(transformer: Transformer,
                                            expected_transformations: TransformationSet) -> None:
    assert transformer.transformations == expected_transformations


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
