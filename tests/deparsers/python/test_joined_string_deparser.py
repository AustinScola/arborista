"""Test arborista.deparsers.python.joined_string_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.joined_string_deparser import JoinedStringDeparser
from arborista.nodes.python.joined_string import JoinedString
from arborista.nodes.python.simple_string import SimpleString


def test_inheritance() -> None:
    """Test arborista.deparsers.python.joined_string_deparser.JoinedStringDeparser inheritance."""
    assert issubclass(JoinedStringDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('joined_string, expected_string', [
    (JoinedString([SimpleString("'foo'"), SimpleString("'bar'")]), "'foo' 'bar'"),
    (JoinedString([SimpleString("'foo'"), SimpleString("'bar'"), SimpleString("'baz'")]), "'foo' 'bar' 'baz'"),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_joined_string(joined_string: JoinedString, expected_string: str) -> None:
    """Test arborista.deparsers.python.joined_string_deparser.JoinedStringDeparser.deparse_joined_string."""  # pylint: disable=line-too-long, useless-suppression
    string: str = JoinedStringDeparser.deparse_joined_string(joined_string)

    assert string == expected_string
