"""Test arborista.nodes.python.positional_parameter."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.positional_parameter.PositionalParameter inheritance."""
    assert issubclass(PositionalParameter, PythonNode)


_PARENT = MagicMock()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_name, expected_annotation, expected_default, expected_parent', [
    ([Name('foo')], {}, Name('foo'), None, None, None),
    ([Name('foo')], {}, Name('foo'), None, None, None),
    ([Name('foo')], {'parent': _PARENT}, Name('foo'), None, None, _PARENT),
    ([Name('foo')], {'annotation': Name('Foo')}, Name('foo'), Name('Foo'), None, None),
    ([Name('foo')], {'default': Name('bar')}, Name('foo'), None, Name('bar'), None),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any], expected_name: Name,
              expected_annotation: Optional[Expression], expected_default: Optional[Expression],
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.positional_parameter.PositionalParameter.__init__."""
    positional_parameter: PositionalParameter = PositionalParameter(*arguments, **keyword_arguments)

    assert positional_parameter.name == expected_name
    assert positional_parameter.annotation == expected_annotation
    assert positional_parameter.default == expected_default
    assert positional_parameter.parent is expected_parent


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
