"""Test arborista.nodes.python.grouped_name_as_names."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.grouped_name_as_names.GroupedNameAsNames inheritance."""
    assert issubclass(GroupedNameAsNames, PythonNode)


# yapf: disable
@pytest.mark.parametrize('name_as_names, parent, pass_parent', [
    (NameAsNames(NameAsName(Name('foo')), []), None, False),
    (NameAsNames(NameAsName(Name('foo')), []), None, True),
    (NameAsNames(NameAsName(Name('foo')), []), MagicMock(), True),
])
# yapf: enable
def test_init(name_as_names: NameAsNames, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.grouped_name_as_names.GroupedNameAsNames.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    grouped_name_as_names: GroupedNameAsNames = GroupedNameAsNames(name_as_names,
                                                                   **keyword_arguments)

    assert grouped_name_as_names.name_as_names == name_as_names
    assert grouped_name_as_names.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('grouped_name_as_names, other, expected_equality', [
    (GroupedNameAsNames(NameAsNames(NameAsName(Name('foo')), [])), 'foo', False),
    (GroupedNameAsNames(NameAsNames(NameAsName(Name('foo')), [])), GroupedNameAsNames(NameAsNames(NameAsName(Name('bar')), [])), False),
    (GroupedNameAsNames(NameAsNames(NameAsName(Name('foo')), [])), GroupedNameAsNames(NameAsNames(NameAsName(Name('foo')), [])), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(grouped_name_as_names: GroupedNameAsNames, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.grouped_name_as_names.GroupedNameAsNames.__eq__."""
    equality: bool = grouped_name_as_names == other

    assert equality == expected_equality
