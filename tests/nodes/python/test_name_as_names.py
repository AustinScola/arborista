"""Test arborista.nodes.python.name_as_names."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.name_as_names.NameAsNames inheritance."""
    assert issubclass(NameAsNames, PythonNode)


# yapf: disable
@pytest.mark.parametrize('first, rest, parent, pass_parent', [
    (NameAsName(Name('foo')), [], None, False),
    (NameAsName(Name('foo')), [], None, True),
    (NameAsName(Name('foo')), [], MagicMock(), True),
])
# yapf: enable
def test_init(first: NameAsName, rest: List[NameAsName], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.name_as_names.NameAsNames.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    name_as_names: NameAsNames = NameAsNames(first, rest, **keyword_arguments)

    assert name_as_names.first == first
    assert name_as_names.rest == rest
    assert name_as_names.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('name_as_names, other, expected_equality', [
    (NameAsNames(NameAsName(Name('foo')), []), 'foo', False),
    (NameAsNames(NameAsName(Name('foo')), []), NameAsNames(NameAsName(Name('foo')), [NameAsName(Name('bar'))]), False),
    (NameAsNames(NameAsName(Name('foo')), [NameAsName(Name('bar'))]), NameAsNames(NameAsName(Name('foo')), [NameAsName(Name('bar'))]), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(name_as_names: NameAsNames, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.name_as_names.NameAsNames.__eq__."""
    equality: bool = name_as_names == other

    assert equality == expected_equality
