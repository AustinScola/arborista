"""Test arborista.nodes.python.name_as_name."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.name_as_name.NameAsName inheritance."""
    assert issubclass(NameAsName, PythonNode)


# yapf: disable
@pytest.mark.parametrize('name, new_name, parent, pass_new_name, pass_parent', [
    (Name('foo'), None, None, False, False),
    (Name('foo'), None, None, False, True),
    (Name('foo'), None, MagicMock(), False, True),
    (Name('foo'), None, None, True, False),
    (Name('foo'), Name('bar'), None, True, False),
])
# yapf: enable
def test_init(name: Name, new_name: Optional[Name], parent: Optional[Node], pass_new_name: bool,
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.name_as_name.NameAsName.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_new_name:
        keyword_arguments['new_name'] = new_name
    if pass_parent:
        keyword_arguments['parent'] = parent

    name_as_name: NameAsName = NameAsName(name, **keyword_arguments)

    assert name_as_name.name == name
    assert name_as_name.new_name == new_name
    assert name_as_name.parent is parent


# yapf: disable
@pytest.mark.parametrize('name_as_name, other, expected_equality', [
    (NameAsName(Name('foo')), 'foo', False),
    (NameAsName(Name('foo')), NameAsName(Name('foo'), Name('bar')), False),
    (NameAsName(Name('foo'), Name('bar')), NameAsName(Name('foo'), Name('bar')), True),
])
# yapf: enable
def test_eq(name_as_name: NameAsName, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.name_as_name.NameAsName.__eq__."""
    equality: bool = name_as_name == other

    assert equality == expected_equality
