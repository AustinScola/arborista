"""Test arborista.nodes.python.parameters."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.parameters.Parameters inheritance."""
    assert issubclass(Parameters, PythonNode)


_parent = MagicMock()


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_positional, expected_parent', [
    ([], {}, [], None),
    ([], {'parent': None}, [], None),
    ([], {'parent': _parent}, [], _parent),
    ([[PositionalParameter(Name('foo'))]], {}, [PositionalParameter(Name('foo'))], None),
])
# yapf: enable
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
              expected_positional: List[PositionalParameter],
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.parameters.Parameters."""
    parameters: Parameters = Parameters(*arguments, **keyword_arguments)

    assert parameters.positional == expected_positional
    assert parameters.parent is expected_parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('parameters, expected_children_list', [
    (Parameters(), []),
    (Parameters([PositionalParameter(Name('x'))]), [PositionalParameter(Name('x'))]),
    (Parameters([PositionalParameter(Name('x')), PositionalParameter(Name('y')), PositionalParameter(Name('z'))]), [PositionalParameter(Name('x')), PositionalParameter(Name('y')), PositionalParameter(Name('z'))])
])
# yapf: enable # pylint: enable=line-too-long
def test_iterate_children(parameters: Parameters, expected_children_list: NodeList) -> None:
    """Test arborista.nodes.python.parameters.iterate_children."""
    children: NodeIterator = parameters.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list
