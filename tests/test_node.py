"""Test arborista.node."""
from typing import Any, Dict, Iterator, Optional, Type, Union
from unittest.mock import MagicMock

import pytest

from arborista.exception import ArboristaException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException
from arborista.node import Node, NodeType, NodeTypes
from arborista.nodes.python.name import Name
from arborista.nodes.python.positional_parameter import PositionalParameter
from testing_helpers.animal_nodes import Animal, Bird, Cat, Dog, Lizard, Mammal
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children


# yapf: disable
@pytest.mark.parametrize('parent, pass_parent, expected_parent', [
    (None, False, None),
    (Animal(), False, None),
    (Animal(), True, Animal()),
])
# yapf: enable
def test_node_init(parent: Optional[Node], pass_parent: bool,
                   expected_parent: Optional[Node]) -> None:
    """Test arborista.node.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    mock_node = MagicMock(Node)
    Node.__init__(mock_node, **keyword_arguments)

    assert mock_node.parent == expected_parent


# yapf: disable
@pytest.mark.parametrize('other', [
    ('foo'),
])
# yapf: enable
def test_eq(other: Any) -> None:
    """Test arborista.node.__eq__."""
    mock_node = MagicMock(Node, __eq__=Node.__eq__)

    with pytest.raises(NotImplementedError):
        mock_node == other  # pylint: disable=pointless-statement


def test_node_iterate_children() -> None:
    """Test arborista.node.iterate_children."""
    mock_node = MagicMock(Node)

    children_iterator: Iterator[Node] = Node.iterate_children(mock_node)

    assert list(children_iterator) == []


# yapf: disable
@pytest.mark.parametrize('node, node_types, expected_exception', [
    (Dog(), Dog, None),
    (Dog(), (Dog,), None),
    (Dog(), (Dog, Mammal), None),
    (Dog(), (Dog, Cat), None),
    (Dog(), (Mammal, Cat), None),
    (Dog(), (Dog, Mammal, Animal), None),
    (Dog(), (Cat, Mammal, Animal), None),
    (Dog(), Cat, UnexpectedNodeTypeException),
    (Dog(), (Cat,), UnexpectedNodeTypeException),
    (Dog(), (Cat, Bird), UnexpectedNodeTypeException),
    (Dog(), (Cat, Bird, Lizard), UnexpectedNodeTypeException),
])
# yapf: enable
def test_assert_is_type(node: Node, node_types: Union[NodeType, NodeTypes],
                        expected_exception: Type[ArboristaException]) -> None:
    """Test arborista.node.Node.assert_is_type."""
    if expected_exception:
        with pytest.raises(expected_exception):
            node.assert_is_type(node_types)
    else:
        node.assert_is_type(node_types)


# yapf: disable
@pytest.mark.parametrize('node', [
    (PositionalParameter(Name('foo'))),
])
# yapf: enable
def test_set_parent_in_children(node: Node) -> None:
    """Test arborista.node.Node.set_parent_in_children."""
    node.set_parent_in_children()

    assert_parent_set_in_children(node)
