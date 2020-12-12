"""Test arborista.node."""
from typing import Iterator, Type, Union

import pytest

from arborista.exception import ArboristaException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException
from arborista.node import Node, NodeType, NodeTypes
from tests.animal_nodes import Animal, Bird, Cat, Dog, Lizard, Mammal


def test_node_iterate_children() -> None:
    """Test arborista.node.iterate_children."""
    node: Node = Node()
    children_iterator: Iterator[Node] = node.iterate_children()
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
