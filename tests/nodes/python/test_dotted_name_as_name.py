"""Test arborista.nodes.python.dotted_name_as_name."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.dotted_name_as_name.DottedNameAsName inheritance."""
    assert issubclass(DottedNameAsName, PythonNode)


# yapf: disable
@pytest.mark.parametrize('dotted_name, name, parent, pass_name, pass_parent', [
    (DottedName(Name('foo'), []), None, None, False, False),
    (DottedName(Name('foo'), []), None, None, False, True),
    (DottedName(Name('foo'), []), None, MagicMock(), False, True),
    (DottedName(Name('foo'), []), None, None, True, False),
    (DottedName(Name('foo'), []), Name('bar'), None, True, False),
    (DottedName(Name('foo'), []), None, None, True, True),
])
# yapf: enable
def test_init(dotted_name: DottedName, name: Optional[Name], parent: Optional[Node],
              pass_name: bool, pass_parent: bool) -> None:
    """Test arborista.nodes.python.dotted_name_as_name.DottedNameAsName.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_name:
        keyword_arguments['name'] = name
    if pass_parent:
        keyword_arguments['parent'] = parent

    dotted_name_as_name: DottedNameAsName = DottedNameAsName(dotted_name, **keyword_arguments)

    assert dotted_name_as_name.dotted_name == dotted_name
    assert dotted_name_as_name.name == name
    assert dotted_name_as_name.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('dotted_name_as_name, other, expected_equality', [
    (DottedNameAsName(DottedName(Name('foo'), [])), 'foo', False),
    (DottedNameAsName(DottedName(Name('foo'), [])), DottedNameAsName(DottedName(Name('foo'), []), Name('bar')), False),
    (DottedNameAsName(DottedName(Name('fooey'), []), Name('bar')), DottedNameAsName(DottedName(Name('foo'), []), Name('bar')), False),
    (DottedNameAsName(DottedName(Name('foo'), []), Name('bar')), DottedNameAsName(DottedName(Name('foo'), []), Name('bar')), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(dotted_name_as_name: DottedNameAsName, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.dotted_name_as_name.DottedNameAsName.__eq__."""
    equality: bool = dotted_name_as_name == other

    assert equality == expected_equality
