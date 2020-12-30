"""Test arborista.parsers.python.integer_parser."""
import libcst
import pytest

from arborista.nodes.python.integer import Integer
from arborista.parser import Parser
from arborista.parsers.python.integer_parser import IntegerParser, LibcstInteger


def test_inheritance() -> None:
    """Test arborista.parsers.python.integer_parser.IntegerParser inheritance."""
    assert issubclass(IntegerParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_integer, expected_integer', [
    (libcst.Integer('1'), Integer(1)),
])
# yapf: enable
def test_parse_integer(libcst_integer: LibcstInteger, expected_integer: Integer) -> None:
    """Test arborista.parsers.python.integer_parser.IntegerParser.parse_integer."""
    integer: Integer = IntegerParser.parse_integer(libcst_integer)

    assert integer == expected_integer
