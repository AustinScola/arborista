"""Test arborista.nodes.python.dotted_name."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name, Names
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.dotted_name.DottedName inheritance."""
    assert issubclass(DottedName, PythonNode)


# yapf: disable
@pytest.mark.parametrize('first_name, rest_of_names, parent, pass_parent', [
    (Name('foo'), [], None, False),
    (Name('foo'), [], None, True),
    (Name('foo'), [], MagicMock(), True),
    (Name('foo'), [Name('bar'), Name('bar')], None, False),
    (Name('foo'), [Name('bar'), Name('bar')], None, True),
    (Name('foo'), [Name('bar'), Name('bar')], MagicMock(), True),
])
# yapf: enable
def test_init(first_name: Name, rest_of_names: Names, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.dotted_name.DottedName.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    dotted_name: DottedName = DottedName(first_name, rest_of_names, **keyword_arguments)

    assert dotted_name.first_name == first_name
    assert dotted_name.rest_of_names == rest_of_names
    assert dotted_name.parent is parent


# yapf: disable
@pytest.mark.parametrize('dotted_name, other, expected_equality', [
    (DottedName(Name('foo'), []), 'foo', False),
    (DottedName(Name('foo'), []), DottedName(Name('foo'), [Name('bar')]), False),
    (DottedName(Name('foo'), [Name('bar')]), DottedName(Name('foo'), [Name('bar')]), True),
])
# yapf: enable
def test_eq(dotted_name: DottedName, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.dotted_name.DottedName.__eq__."""
    equality: bool = dotted_name == other

    assert equality == expected_equality
