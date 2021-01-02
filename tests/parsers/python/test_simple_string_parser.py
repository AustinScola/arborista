"""Test arborista.parsers.python.simple_string_parser."""
import libcst
import pytest

from arborista.nodes.python.simple_string import SimpleString
from arborista.parser import Parser
from arborista.parsers.python.simple_string_parser import LibcstSimpleString, SimpleStringParser


def test_inheritance() -> None:
    """Test arborista.parsers.python.simple_string_parser.SimpleStringParser inheritance."""
    assert issubclass(SimpleStringParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_simple_string, expected_simple_string', [
    (libcst.SimpleString("'foo'"), SimpleString("'foo'")),
])
# yapf: enable
def test_parse_simple_string(libcst_simple_string: LibcstSimpleString,
                             expected_simple_string: SimpleString) -> None:
    """Test arborista.parsers.python.simple_string_parser.SimpleStringParser.parse_simple_string."""
    simple_string: SimpleString = SimpleStringParser.parse_simple_string(libcst_simple_string)

    assert simple_string == expected_simple_string
