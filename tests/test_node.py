"""Test arborista.node."""
from typing import Any, Dict, Iterator, Optional, Type, Union

import pytest

from arborista.exception import ArboristaException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException
from arborista.node import Node, NodeType, NodeTypes
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children
from tests.animal_nodes import Animal, Bird, Cat, Dog, Lizard, Mammal


# yapf: disable
@pytest.mark.parametrize('parent, pass_parent, expected_parent', [
    (None, False, None),
    (Animal(), False, None),
    (Animal(), True, Animal()),
])
# yapf: enable
def test_node_init(parent: Optional[Node], pass_parent: bool,
                   expected_parent: Optional[Node]) -> None:
    """Test arborista.node.iterate_children."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent
    print(keyword_arguments)
    node: Node = Node(**keyword_arguments)

    assert node.parent == expected_parent


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


# yapf: disable
@pytest.mark.parametrize('node', [
    (Parameter(Name('foo'))),
])
# yapf: enable
def test_set_parent_in_children(node: Node) -> None:
    """Test arborista.node.Node.set_parent_in_children."""
    node.set_parent_in_children()

    assert_parent_set_in_children(node)
