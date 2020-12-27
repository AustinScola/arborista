"""Test arborista.transformations.python.deparsers.module_to_string."""
from pathlib import Path
from typing import Optional, Type

import pytest

from arborista.exception import ArboristaException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException
from arborista.node import Node
from arborista.nodes.file_system.file import File
from arborista.nodes.python.module import Module
from arborista.nodes.sequences.text.string import String
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult
from arborista.transformations.python.deparsers.module_to_string import ModuleToString
from arborista.tree import Tree


def test_inheritance() -> None:
    """Test arborista.transformations.python.deparsers.module_to_string.ModuleToString inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ModuleToString, Transformation)


def test_node_types() -> None:
    """Test arborista.transformations.python.deparsers.module_to_string.ModuleToString.NODE_TYPES."""  # pylint: disable=line-too-long, useless-suppression
    assert ModuleToString.NODE_TYPES == {Module}


node_0: Node = File(Path('foo.py'), String())
tree_0: Tree = Tree(root=node_0)
expected_transformation_result_0: Optional[TransformationResult] = None
expected_tree_0: Tree = Tree(root=node_0)
expected_exception_0: Optional[Type[ArboristaException]] = UnexpectedNodeTypeException

node_1: Node = Module('foo', [])
file_1: File = File(Path('foo.py'), node_1)
node_1.parent = file_1
tree_1: Tree = Tree(root=file_1)
expected_transformation_result_1: Optional[TransformationResult] = TransformationResult(
    String(), True, [node_1])
expected_tree_1: Tree = Tree(root=File(Path('foo.py'), String()))
expected_exception_1: Optional[Type[ArboristaException]] = None


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('tree, node, expected_transformation_result, expected_tree, expected_exception', [
    (tree_0, node_0, expected_transformation_result_0, expected_tree_0, expected_exception_0),
    (tree_1, node_1, expected_transformation_result_1, expected_tree_1, expected_exception_1),
])
# yapf: enable # pylint: enable=line-too-long
def test_maybe_transform(tree: Tree, node: Node,
                         expected_transformation_result: Optional[TransformationResult],
                         expected_tree: Tree,
                         expected_exception: Optional[Type[ArboristaException]]) -> None:
    """Test arborista.transformations.python.deparsers.module_to_string.ModuleToString.maybe_transform."""  # pylint: disable=line-too-long, useless-suppression
    if expected_exception:
        with pytest.raises(expected_exception):
            ModuleToString.maybe_transform(node)
    else:
        transformation_result: TransformationResult = ModuleToString.maybe_transform(node)

        assert transformation_result == expected_transformation_result

    assert tree == expected_tree
