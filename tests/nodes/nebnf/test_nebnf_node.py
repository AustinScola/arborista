"""Test arborista.nodes.nebnf.nebnf_node."""
from abc import ABC
from typing import Any, Dict

import pytest
from seligimus.python.classes.attributes import set_attributes

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.nebnf_node.NEBNFNode inheritance."""
    assert issubclass(NEBNFNode, (Node, ABC))


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('self_class_name, other_class_name, self_attributes, other_attributes, expected_equality', [
    ('Foo', 'Bar', {'parent': 1}, {'parent': 1}, False),
    ('Foo', 'Foo', {'parent': 1, 'wibble': 2}, {'parent': 1, 'wibble': 3}, False),
    ('Foo', 'Foo', {'parent': 1}, {'parent': 2}, True),
    ('Foo', 'Foo', {'parent': 1, 'wibble': 2}, {'parent': 1, 'wibble': 2}, True),
    ('Foo', 'Foo', {'parent': 1, 'wibble': 2}, {'parent': 2, 'wibble': 2}, True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(self_class_name: str, other_class_name: str, self_attributes: Dict[str, Any],
            other_attributes: Dict[str, Any], expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.nebnf_node.NEBNFNode.__eq__."""
    self_type = type(self_class_name, tuple(), {})
    self = self_type()
    set_attributes(self, self_attributes)

    if other_class_name == self_class_name:
        other_type = self_type
    else:
        other_type = type(other_class_name, tuple(), {})
    other = other_type()
    set_attributes(other, other_attributes)

    equality: bool = NEBNFNode.__eq__(self, other)

    assert equality == expected_equality
