"""Test arborista.nodes.python.positional_parameter."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.name import Name
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.positional_parameter.PositionalParameter inheritance."""
    assert issubclass(PositionalParameter, PythonNode)


# yapf: disable
@pytest.mark.parametrize('name, parent, pass_parent', [
    (Name('foo'), None, False),
    (Name('foo'), None, True),
    (Name('foo'), MagicMock(), True),
])
# yapf: enable
def test_init(name: Name, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.positional_parameter.PositionalParameter.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    positional_parameter: PositionalParameter = PositionalParameter(name, **keyword_arguments)

    assert positional_parameter.name == name
    assert positional_parameter.parent is parent


# yapf: disable
@pytest.mark.parametrize('positional_parameter, expected_children_list', [
    (PositionalParameter(Name('foo')), [Name('foo')]),
])
# yapf: enable
def test_iterate_children(positional_parameter: PositionalParameter,
                          expected_children_list: NodeList) -> None:
    """Test arborista.nodes.python.positional_parameter.PositionalParameter.iterate_children."""
    children: NodeIterator = positional_parameter.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list
