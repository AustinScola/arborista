"""Test arborista.transformations.python.parsers.file_to_module."""
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
from arborista.transformations.python.parsers.file_to_module import FileToModule
from arborista.tree import Tree


def test_inheritance() -> None:
    """Test arborista.transformations.python.parsers.file_to_module.FileToModule inheritance."""
    assert issubclass(FileToModule, Transformation)


def test_node_types() -> None:
    """Test arborista.transformations.python.parsers.file_to_module.FileToModule.NODE_TYPES."""
    FileToModule.NODE_TYPES = {File}


node_0: Node = Module('foo')
tree_0: Tree = Tree(root=node_0)
expected_transformation_result_0: Optional[TransformationResult] = None
expected_tree_0: Tree = Tree(root=Module('foo'))
expected_exception_0: Optional[Type[ArboristaException]] = UnexpectedNodeTypeException

string_node_1 = String()
node_1: Node = File(Path('foo.py'), string_node_1)
tree_1: Tree = Tree(root=node_1)
expected_transformation_result_1: Optional[TransformationResult] = TransformationResult(
    File(Path('foo.py'), Module('foo', [])), True, [string_node_1])
expected_tree_1: Tree = Tree(root=File(Path('foo.py'), Module('foo', [])))
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
    """Test arborista.transformations.python.parsers.file_to_module.FileToModule.maybe_transform."""
    if expected_exception:
        with pytest.raises(expected_exception):
            FileToModule.maybe_transform(node)
    else:
        transformation_result: TransformationResult = FileToModule.maybe_transform(node)

        assert transformation_result == expected_transformation_result

    assert tree == expected_tree
