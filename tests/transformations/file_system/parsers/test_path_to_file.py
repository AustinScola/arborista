"""Test arborista.transformations.file_system.parsers.path_to_file."""
from pathlib import Path
from typing import Optional, Type
from unittest.mock import mock_open, patch

import pytest

from arborista.exception import ArboristaException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException
from arborista.node import Node
from arborista.nodes.file_system.file import File
from arborista.nodes.file_system.path_node import PathNode
from arborista.nodes.sequences.text.string import String
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult
from arborista.transformations.file_system.parsers.path_to_file import PathToFile
from arborista.tree import Tree


def test_inheritance() -> None:
    """Test arborista.transformations.file_system.parsers.path_to_file.PathToFile inheritance."""
    assert issubclass(PathToFile, Transformation)


def test_node_types() -> None:
    """Test arborista.transformations.file_system.parsers.path_to_file.PathToFile.NODE_TYPES."""
    assert PathToFile.NODE_TYPES == {PathNode}


file_contents_0: Optional[str] = None
node_0: Node = File(Path('foo.py'), String())
tree_0: Tree = Tree(root=node_0)
expected_transformation_result_0: Optional[TransformationResult] = None
expected_tree_0: Tree = Tree(root=File(Path('foo.py'), String()))
expected_exception_0: Optional[Type[ArboristaException]] = UnexpectedNodeTypeException

file_contents_1: Optional[str] = 'def foo(): return'
node_1: Node = PathNode(Path('foo.py'))
tree_1: Tree = Tree(root=node_1)
expected_transformation_result_1: Optional[TransformationResult] = TransformationResult(
    File(Path('foo.py'), String('def foo(): return')), True, [node_1])
expected_tree_1: Tree = Tree(root=PathNode(Path('foo.py')))
expected_exception_1: Optional[Type[ArboristaException]] = None


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('file_contents, tree, node, expected_transformation_result, expected_tree, expected_exception', [
    (file_contents_0, tree_0, node_0, expected_transformation_result_0, expected_tree_0, expected_exception_0),
    (file_contents_1, tree_1, node_1, expected_transformation_result_1, expected_tree_1, expected_exception_1),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_maybe_transform(file_contents: Optional[str], tree: Tree, node: Node,
                         expected_transformation_result: Optional[TransformationResult],
                         expected_tree: Tree,
                         expected_exception: Optional[Type[ArboristaException]]) -> None:
    """Test arborista.transformations.file_system.parsers.path_to_file.PathToFile.maybe_transform."""  # pylint: disable=line-too-long, useless-suppression
    with patch('builtins.open', mock_open(read_data=file_contents)):
        if expected_exception:
            with pytest.raises(expected_exception):
                PathToFile.maybe_transform(node)
        else:
            transformation_result: TransformationResult = PathToFile.maybe_transform(node)

            assert transformation_result == expected_transformation_result

        assert tree == expected_tree
