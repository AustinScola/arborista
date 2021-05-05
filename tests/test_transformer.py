"""Test arborista.transformer."""
from pathlib import Path
from typing import Dict

import pytest

from arborista.node import NodeType
from arborista.nodes.file_system.file import File
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.module import Module
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.sequences.text.string import String
from arborista.transformation import Transformations, TransformationSet
from arborista.transformations.python.deparsers.module_to_string import ModuleToString
from arborista.transformations.python.trim_after_return import TrimAfterReturn
from arborista.transformer import Transformer
from arborista.tree import Tree


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('transformations, expected_transformations, expected_node_type_to_transformation', [
    ([], set(), {}),
    ([TrimAfterReturn], set([TrimAfterReturn]), {ReturnStatement: {TrimAfterReturn}}),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(transformations: Transformations, expected_transformations: TransformationSet,
              expected_node_type_to_transformation: Dict[NodeType, TransformationSet]) -> None:
    """Test arborista.transformer.Transformer.__init__."""
    transformer: Transformer = Transformer(transformations)

    _assert_transformer_has_transformations(transformer, expected_transformations)
    _assert_transformer_has_node_type_to_transformations(transformer,
                                                         expected_node_type_to_transformation)


def _assert_transformer_has_transformations(transformer: Transformer,
                                            expected_transformations: TransformationSet) -> None:
    assert transformer.transformations == expected_transformations


def _assert_transformer_has_node_type_to_transformations(
        transformer: Transformer,
        expected_node_type_to_transformation: Dict[NodeType, TransformationSet]) -> None:
    assert transformer._node_type_to_transformations == expected_node_type_to_transformation  # pylint: disable=protected-access


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('transformations, tree, expected_transformed_tree', [
    ([TrimAfterReturn], Tree(root=FunctionDefinition(Name('foo'), parameters=Parameters(), body=SimpleStatement([ReturnStatement(), ReturnStatement()]))), Tree(root=FunctionDefinition(Name('foo'), parameters=Parameters(), body=SimpleStatement([ReturnStatement()])))),
    ([ModuleToString], Tree(root=File(Path('foo.py'), Module('foo', []))), Tree(root=File(Path('foo.py'), String()))),
    ([ModuleToString], Tree(root=Module('foo', [])), Tree(root=String())),
])
# yapf: enable # pylint: enable=line-too-long
def test_run(transformations: Transformations, tree: Tree, expected_transformed_tree: Tree) -> None:
    """Test arborista.transformer.Transformer.run."""
    transformer: Transformer = Transformer(transformations)

    transformed_tree: Tree = transformer.run(tree)

    assert transformed_tree == expected_transformed_tree


# yapf: disable
@pytest.mark.parametrize('transformations, node_type, expected_transformations_for_node_type', [
    ([], Module, set()),
    ([TrimAfterReturn], ReturnStatement, {TrimAfterReturn}),
])
# yapf: enable
def test_get_transformations_for_node_type(
        transformations: Transformations, node_type: NodeType,
        expected_transformations_for_node_type: Transformations) -> None:
    """Test arborista.transformer.Transformer._get_transformations_for_node_type."""
    transformer: Transformer = Transformer(transformations)

    transformations_for_node_type: Transformations = transformer._get_transformations_for_node_type(  # pylint: disable=protected-access
        node_type)

    assert transformations_for_node_type == expected_transformations_for_node_type
