"""Test arborista.nodes.python.joined_string."""
from typing import Any, Dict, Iterable, Iterator, List, Optional, Union

import pytest

from arborista.node import Node
from arborista.nodes.python.formatted_string import FormattedString
from arborista.nodes.python.joined_string import JoinedString
from arborista.nodes.python.simple_string import SimpleString, SimpleStringList
from arborista.nodes.python.string import String
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.python.joined_string.JoinedString inheritance."""
    assert issubclass(JoinedString, String)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('joined_string, expected_children_list', [
    (JoinedString([]), []),
    (JoinedString([SimpleString('foo')]), [SimpleString('foo')]),
    (JoinedString([SimpleString('foo'), SimpleString('bar'), SimpleString('baz')]), [SimpleString('foo'), SimpleString('bar'), SimpleString('baz')]),
])
# yapf: enable # pylint: enable=line-too-long
def test_iterate_children(
        joined_string: JoinedString, expected_children_list: List[Union[SimpleString,
                                                                        FormattedString]]) -> None:
    """Test arborista.nodes.python.joined_string.JoinedString.iterate_children."""
    children: Iterator[Union[SimpleString, FormattedString]] = joined_string.iterate_children()
    children_list: List[Union[SimpleString, FormattedString]] = list(children)

    assert children_list == expected_children_list


# yapf: disable
@pytest.mark.parametrize('strings, parent, pass_parent, expected_strings', [
    ([SimpleString()], None, False, [SimpleString()]),
    ([], Dog(), True, []),
    ([SimpleString()], Dog(), True, [SimpleString()]),
])
# yapf: enable
def test_init(strings: Iterable[Union[SimpleString, FormattedString]], parent: Optional[Node],
              pass_parent: bool, expected_strings: SimpleStringList) -> None:
    """Test arborista.nodes.python.joined_string.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    joined_string = JoinedString(strings, **keyword_arguments)

    assert joined_string.parent is parent
    assert joined_string.strings == expected_strings


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('joined_string, other, expected_equality', [
    (JoinedString([]), 'foo', False),
    (JoinedString([]), JoinedString([SimpleString('foo')]), False),
    (JoinedString([SimpleString('foo')]), JoinedString([]), False),
    (JoinedString([SimpleString()]), JoinedString([SimpleString()]), True),
    (JoinedString([SimpleString('foo')]), JoinedString([SimpleString('bar')]), False),
    (JoinedString([SimpleString('foo')]), JoinedString([SimpleString('foo')]), True),
    (JoinedString([SimpleString()]), JoinedString([SimpleString(), SimpleString()]), False),
    (JoinedString([SimpleString(), SimpleString()]), JoinedString([SimpleString(), SimpleString()]), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(joined_string: JoinedString, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.joined_string.__eq__."""
    equality: bool = joined_string == other

    assert equality == expected_equality
