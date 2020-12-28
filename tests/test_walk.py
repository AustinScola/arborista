"""Test arborista.walk."""
import pytest

from arborista.node import NodeIterator, NodeList
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.tree import Tree
from arborista.walk import Walk
from testing_helpers.assert_nodes_match import assert_nodes_match


# yapf: disable
@pytest.mark.parametrize('tree', [
    (Tree(),),
    (Tree(SimpleStatement([]))),
])
# yapf: enable
def test_init(tree: Tree) -> None:
    """Test arborista.walk.Walk.__init__."""
    walk: Walk = Walk(tree)

    assert walk.tree == tree


# yapf: disable
@pytest.mark.parametrize('tree', [
    (Tree()),
    (Tree(SimpleStatement([]))),
])
# yapf: enable
def test_iter(tree: Tree) -> None:
    """Test arborista.walk.Walk.__iter__."""
    walk: Walk = Walk(tree)

    steps: NodeIterator = iter(walk)

    assert steps == walk


# yapf: disable
@pytest.mark.parametrize('tree, expected_steps', [
    (Tree(), []),
    (Tree(SimpleStatement([])), [SimpleStatement([])]),
])
# yapf: enable
def test_next(tree: Tree, expected_steps: NodeList) -> None:
    """Test arborista.walk.Walk.__next__."""
    walk: Walk = Walk(tree)

    steps: NodeIterator = iter(walk)

    assert_nodes_match(steps, expected_steps)
