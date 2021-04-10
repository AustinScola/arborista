"""Test arborista.nodes.python.joined_string."""
from typing import Any, Dict, Iterable, Iterator, List, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.joined_string import JoinedString
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.python.joined_string.JoinedString inheritance."""
    assert issubclass(JoinedString, Expression)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('joined_string, expected_children_list', [
    (JoinedString([]), []),
    (JoinedString([String(None, SingleQuotedShortString('foo'))]), [String(None, SingleQuotedShortString('foo'))]),
    (JoinedString([String(None, SingleQuotedShortString('foo')), String(None, SingleQuotedShortString('bar')), String(None, SingleQuotedShortString('baz'))]), [String(None, SingleQuotedShortString('foo')), String(None, SingleQuotedShortString('bar')), String(None, SingleQuotedShortString('baz'))]),
])
# yapf: enable # pylint: enable=line-too-long
def test_iterate_children(joined_string: JoinedString,
                          expected_children_list: List[String]) -> None:
    """Test arborista.nodes.python.joined_string.JoinedString.iterate_children."""
    children: Iterator[String] = joined_string.iterate_children()
    children_list: List[String] = list(children)

    assert children_list == expected_children_list


# yapf: disable
@pytest.mark.parametrize('strings, parent, pass_parent, expected_strings', [
    ([SingleQuotedShortString('')], None, False, [SingleQuotedShortString('')]),
    ([], Dog(), True, []),
    ([SingleQuotedShortString('')], Dog(), True, [SingleQuotedShortString('')]),
])
# yapf: enable
def test_init(strings: Iterable[String], parent: Optional[Node], pass_parent: bool,
              expected_strings: List[String]) -> None:
    """Test arborista.nodes.python.joined_string.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    joined_string = JoinedString(strings, **keyword_arguments)

    assert joined_string.strings == expected_strings
    assert joined_string.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('joined_string, other, expected_equality', [
    (JoinedString([]), 'foo', False),
    (JoinedString([]), JoinedString([String(None, SingleQuotedShortString('foo'))]), False),
    (JoinedString([String(None, SingleQuotedShortString('foo'))]), JoinedString([]), False),
    (JoinedString([String(None, SingleQuotedShortString(''))]), JoinedString([String(None, SingleQuotedShortString(''))]), True),
    (JoinedString([String(None, SingleQuotedShortString('foo'))]), JoinedString([String(None, SingleQuotedShortString('bar'))]), False),
    (JoinedString([String(None, SingleQuotedShortString('foo'))]), JoinedString([String(None, SingleQuotedShortString('foo'))]), True),
    (JoinedString([String(None, SingleQuotedShortString(''))]), JoinedString([String(None, SingleQuotedShortString('')), String(None, SingleQuotedShortString(''))]), False),
    (JoinedString([String(None, SingleQuotedShortString('')), String(None, SingleQuotedShortString(''))]), JoinedString([String(None, SingleQuotedShortString('')), String(None, SingleQuotedShortString(''))]), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(joined_string: JoinedString, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.joined_string.__eq__."""
    equality: bool = joined_string == other

    assert equality == expected_equality
