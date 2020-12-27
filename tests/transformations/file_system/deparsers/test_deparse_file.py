"""Test arborista.transformations.file_system.deparsers.deparse_file."""
from pathlib import Path
from typing import Optional, Type
from unittest.mock import mock_open, patch

import pytest

from arborista.exception import ArboristaException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException
from arborista.node import Node
from arborista.nodes.file_system.file import File
from arborista.nodes.python.module import Module
from arborista.nodes.sequences.text.string import String
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult
from arborista.transformations.file_system.deparsers.deparse_file import DeparseFile
from arborista.tree import Tree


def test_inheritance() -> None:
    """Test arborista.transformations.file_system.deparsers.deparse_file.DeparseFile inheritance."""
    assert issubclass(DeparseFile, Transformation)


def test_node_types() -> None:
    """Test arborista.transformations.file_system.deparsers.deparse_file.DeparseFile.NODE_TYPES."""
    assert DeparseFile.NODE_TYPES == {File}


node_0: Node = String()
tree_0: Tree = Tree(root=node_0)
expected_transformation_result_0: Optional[TransformationResult] = None
expected_tree_0: Tree = Tree(root=node_0)
expected_file_0: Optional[Path] = None
expected_file_contents_0: Optional[str] = None
expected_exception_0: Optional[Type[ArboristaException]] = UnexpectedNodeTypeException

node_1: Node = File(Path('foo.py'), Module('foo', []))
tree_1: Tree = Tree(root=node_1)
expected_transformation_result_1: Optional[TransformationResult] = TransformationResult(
    File(Path('foo.py'), Module('foo', [])), False, [])
expected_tree_1: Tree = Tree(root=node_1)
expected_file_1: Optional[Path] = None
expected_file_contents_1: Optional[str] = None
expected_exception_1: Optional[Type[ArboristaException]] = None

node_2: Node = File(Path('foo.py'), String(''))
tree_2: Tree = Tree(root=node_2)
expected_transformation_result_2: Optional[TransformationResult] = TransformationResult(
    None, True, [node_2])
expected_tree_2: Tree = Tree(root=node_2)
expected_file_2: Optional[Path] = Path('foo.py')
expected_file_contents_2: Optional[str] = ''
expected_exception_2: Optional[Type[ArboristaException]] = None

node_3: Node = File(Path('foo.py'), String('def foo(): return'))
tree_3: Tree = Tree(root=node_3)
expected_transformation_result_3: Optional[TransformationResult] = TransformationResult(
    None, True, [node_3])
expected_tree_3: Tree = Tree(root=node_3)
expected_file_3: Optional[Path] = Path('foo.py')
expected_file_contents_3: Optional[str] = 'def foo(): return'
expected_exception_3: Optional[Type[ArboristaException]] = None


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('tree, node, expected_transformation_result, expected_tree, expected_file, expected_file_contents, expected_exception', [
    (tree_0, node_0, expected_transformation_result_0, expected_tree_0, expected_file_0, expected_file_contents_0, expected_exception_0),
    (tree_1, node_1, expected_transformation_result_1, expected_tree_1, expected_file_1, expected_file_contents_1, expected_exception_1),
    (tree_2, node_2, expected_transformation_result_2, expected_tree_2, expected_file_2, expected_file_contents_2, expected_exception_2),
    (tree_3, node_3, expected_transformation_result_3, expected_tree_3, expected_file_3, expected_file_contents_3, expected_exception_3),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_maybe_transform(tree: Tree, node: Node,
                         expected_transformation_result: Optional[TransformationResult],
                         expected_tree: Tree, expected_file: Optional[Path],
                         expected_file_contents: Optional[str],
                         expected_exception: Optional[Type[ArboristaException]]) -> None:
    """Test arborista.transformations.file_system.deparsers.deparse_file.DeparseFile.maybe_transform."""  # pylint: disable=line-too-long, useless-suppression
    with patch('builtins.open', mock_open()) as open_mock:
        if expected_exception:
            with pytest.raises(expected_exception):
                DeparseFile.maybe_transform(node)
        else:
            transformation_result: TransformationResult = DeparseFile.maybe_transform(node)

            assert transformation_result == expected_transformation_result

            if expected_file is not None:
                open_mock.assert_called_once_with(expected_file, mode='w')

                system_file_mock = open_mock()
                system_file_mock.write.assert_called_once_with(expected_file_contents)

        assert tree == expected_tree
