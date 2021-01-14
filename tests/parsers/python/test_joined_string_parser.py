"""Test arborista.parsers.python.joined_string_parser."""
import libcst
import pytest

from arborista.nodes.python.joined_string import JoinedString
from arborista.nodes.python.simple_string import SimpleString
from arborista.parser import Parser
from arborista.parsers.python.joined_string_parser import JoinedStringParser, LibcstJoinedString


def test_inheritance() -> None:
    """Test arborista.parsers.python.joined_string_parser.JoinedStringParser inheritance."""
    assert issubclass(JoinedStringParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_joined_string, expected_joined_string', [
    (libcst.ConcatenatedString(libcst.SimpleString("'foo'"), libcst.SimpleString("'bar'")), JoinedString([SimpleString("'foo'"), SimpleString("'bar'")])),
    (libcst.ConcatenatedString(libcst.SimpleString("'foo'"), libcst.ConcatenatedString(libcst.SimpleString("'bar'"), libcst.SimpleString("'baz'"))), JoinedString([SimpleString("'foo'"), SimpleString("'bar'"), SimpleString("'baz'")])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_joined_string(libcst_joined_string: LibcstJoinedString,
                             expected_joined_string: JoinedString) -> None:
    """Test arborista.parsers.python.joined_string_parser.JoinedStringParser.parse_joined_string."""
    joined_string: JoinedString = JoinedStringParser.parse_joined_string(libcst_joined_string)

    assert joined_string == expected_joined_string
