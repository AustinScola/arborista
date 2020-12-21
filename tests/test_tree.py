"""Test arborista.tree."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.module import Module
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.tree import Tree
from testing_helpers.animal_nodes import Dog
from testing_helpers.assert_nodes_match_expected_nodes import assert_nodes_match_expected_nodes
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children


# yapf: disable
@pytest.mark.parametrize('root, pass_root, expected_root', [
    (None, False, None),
    (None, True, None),
    (Dog(), True, Dog()),
])
# yapf: enable
def test_init(root: Optional[Node], pass_root: bool, expected_root: Optional[Node]) -> None:
    """Test arborista.tree.Tree.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_root:
        keyword_arguments['root'] = root

    tree: Tree = Tree(**keyword_arguments)

    assert tree.root == expected_root


# yapf: disable
@pytest.mark.parametrize('tree, other, expected_equality', [
    (Tree(root=None), 'foo', False),
    (Tree(root=None), Tree(root=Module('foo')), False),
    (Tree(root=Module('foo')), Tree(root=Module('bar')), False),
    (Tree(root=None), Tree(root=None), True),
    (Tree(root=Module('foo')), Tree(root=Module('foo')), True),
])
# yapf: enable
def test_eq(tree: Tree, other: Any, expected_equality: bool) -> None:
    """Test arborista.tree.Tree.__eq__."""
    equality: bool = tree == other
    assert equality == expected_equality


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('tree, expected_nodes', [
    (Tree(), []),
    (Tree(SimpleStatement([])), [SimpleStatement([])]),
    (Tree(SimpleStatement([ReturnStatement()])), [SimpleStatement([ReturnStatement()]), ReturnStatement()]),
    (Tree(SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()])), [SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()]), ReturnStatement(), ReturnStatement(), ReturnStatement()]),
    (Tree(SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()])), [SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()]), ReturnStatement(), ReturnStatement(), ReturnStatement()]),
    (Tree(FunctionDefinition(Name('foo'), parameters=[Parameter(Name('a'))], body=SimpleStatement([ReturnStatement()]))), [FunctionDefinition(Name('foo'), parameters=[Parameter(Name('a'))], body=SimpleStatement([ReturnStatement()])), Name('foo'), Parameter(Name('a')), Name('a'), SimpleStatement([ReturnStatement()]), ReturnStatement()]),
])
# yapf: enable # pylint: enable=line-too-long
def test_walk(tree: Tree, expected_nodes: NodeList) -> None:
    """Test arborista.tree.Tree.walk."""
    nodes: NodeIterator = tree.walk()

    assert_nodes_match_expected_nodes(nodes, expected_nodes)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('tree', [
    (Tree()),
    (Tree(SimpleStatement([]))),
    (Tree(SimpleStatement([ReturnStatement()]))),
    (Tree(SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()]))),
    (Tree(SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()]))),
    (Tree(FunctionDefinition(Name('foo'), parameters=[Parameter(Name('a'))], body=SimpleStatement([ReturnStatement()])))),
])
# yapf: enable # pylint: enable=line-too-long
def test_set_parents(tree: Tree) -> None:
    """Test arborista.tree.Tree.set_parents."""
    tree.set_parents()

    for node in tree.walk():
        assert_parent_set_in_children(node)
