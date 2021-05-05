"""Test arborista.transformations.python.trim_after_return."""
from typing import Optional, Type

import pytest

from arborista.exception import ArboristaException
from arborista.exceptions.cannot_find_child_exception import CannotFindChildException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException
from arborista.node import Node
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult
from arborista.transformations.python.trim_after_return import TrimAfterReturn
from arborista.tree import Tree


def test_node_types() -> None:
    """Test arborista.python.transformations.trim_after_return.TrimAfterReturn.NODE_TYPES."""
    assert TrimAfterReturn.NODE_TYPES == {ReturnStatement}


def test_inheritance() -> None:
    """Test arborista.python.transformations.trim_after_return.TrimAfterReturn."""
    assert issubclass(TrimAfterReturn, Transformation)


node_0: Node = FunctionDefinition(Name('foo'), Parameters(), SimpleStatement([]))
tree_0: Tree = Tree(root=node_0)
expected_transformation_result_0: Optional[TransformationResult] = None
expected_tree_0: Tree = Tree(root=node_0)
expected_exception_0: Optional[Type[ArboristaException]] = UnexpectedNodeTypeException

node_1: ReturnStatement = ReturnStatement()
tree_1: Tree = Tree(root=SimpleStatement([node_1]))
node_1.parent = tree_1.root
expected_transformation_result_1: Optional[TransformationResult] = TransformationResult(
    ReturnStatement(), False, [])
expected_tree_1: Tree = Tree(root=SimpleStatement([ReturnStatement()]))
expected_exception_1: Optional[Type[ArboristaException]] = None

node_2: ReturnStatement = ReturnStatement()
removed_nodes_2 = [ReturnStatement()]
tree_2: Tree = Tree(root=SimpleStatement([node_2] + removed_nodes_2))
node_2.parent = tree_2.root
expected_transformation_result_2: Optional[TransformationResult] = TransformationResult(
    ReturnStatement(), True, removed_nodes_2)
expected_tree_2: Tree = Tree(root=SimpleStatement([ReturnStatement()]))
expected_exception_2: Optional[Type[ArboristaException]] = None

node_3: ReturnStatement = ReturnStatement()
tree_3: Tree = Tree(root=SimpleStatement([ReturnStatement(), node_3]))
node_3.parent = tree_3.root
expected_transformation_result_3: Optional[TransformationResult] = TransformationResult(
    node_3, False, [])
expected_tree_3: Tree = Tree(root=SimpleStatement([ReturnStatement(), ReturnStatement()]))
expected_exception_3: Optional[Type[ArboristaException]] = None

node_4: ReturnStatement = ReturnStatement()
removed_nodes_4 = [ReturnStatement(), ReturnStatement()]
tree_4: Tree = Tree(root=SimpleStatement([node_4] + removed_nodes_4))
node_4.parent = tree_4.root
expected_transformation_result_4: Optional[TransformationResult] = TransformationResult(
    node_4, True, removed_nodes_4)
expected_tree_4: Tree = Tree(root=SimpleStatement([ReturnStatement()]))
expected_exception_4: Optional[Type[ArboristaException]] = None

node_5: ReturnStatement = ReturnStatement()
removed_nodes_5 = [ReturnStatement()]
tree_5: Tree = Tree(root=SimpleStatement([ReturnStatement(), node_5] + removed_nodes_5))
node_5.parent = tree_5.root
expected_transformation_result_5: Optional[TransformationResult] = TransformationResult(
    ReturnStatement(), True, removed_nodes_5)
expected_tree_5: Tree = Tree(root=SimpleStatement([ReturnStatement(), ReturnStatement()]))
expected_exception_5: Optional[Type[ArboristaException]] = None

node_6: ReturnStatement = ReturnStatement()
tree_6: Tree = Tree(root=SimpleStatement([ReturnStatement(), ReturnStatement(), node_6]))
node_6.parent = tree_6.root
expected_transformation_result_6: Optional[TransformationResult] = TransformationResult(
    node_6, False, [])
expected_tree_6: Tree = Tree(root=SimpleStatement(
    [ReturnStatement(), ReturnStatement(), ReturnStatement()]))
expected_exception_6: Optional[Type[ArboristaException]] = None

node_7: ReturnStatement = ReturnStatement()
tree_7: Tree = Tree(root=SimpleStatement([ReturnStatement()]))
node_7.parent = tree_7.root
expected_transformation_result_7: Optional[TransformationResult] = None
expected_tree_7: Tree = Tree(root=SimpleStatement([ReturnStatement()]))
expected_exception_7: Optional[Type[ArboristaException]] = CannotFindChildException


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('tree, node, expected_transformation_result, expected_tree, expected_exception', [
    (tree_0, node_0, expected_transformation_result_0, expected_tree_0, expected_exception_0),
    (tree_1, node_1, expected_transformation_result_1, expected_tree_1, expected_exception_1),
    (tree_2, node_2, expected_transformation_result_2, expected_tree_2, expected_exception_2),
    (tree_3, node_3, expected_transformation_result_3, expected_tree_3, expected_exception_3),
    (tree_4, node_4, expected_transformation_result_4, expected_tree_4, expected_exception_4),
    (tree_5, node_5, expected_transformation_result_5, expected_tree_5, expected_exception_5),
    (tree_6, node_6, expected_transformation_result_6, expected_tree_6, expected_exception_6),
    (tree_7, node_7, expected_transformation_result_7, expected_tree_7, expected_exception_7),
])
# yapf: enable # pylint: enable=line-too-long
def test_maybe_transform(tree: Tree, node: Node,
                         expected_transformation_result: Optional[TransformationResult],
                         expected_tree: Tree,
                         expected_exception: Optional[Type[ArboristaException]]) -> None:
    """Test arborista.python.transformations.trim_after_return.TrimAfterReturn.maybe_transform."""
    if expected_exception:
        with pytest.raises(expected_exception):
            TrimAfterReturn.maybe_transform(node)
    else:
        transformation_result: TransformationResult = TrimAfterReturn.maybe_transform(node)

        assert transformation_result == expected_transformation_result

    assert tree == expected_tree
