"""Test arborista.parsers.python.equals_parser."""
import libcst
import pytest

from arborista.nodes.python.equals import Equals
from arborista.parser import Parser
from arborista.parsers.python.equals_parser import EqualsParser, LibcstEquals


def test_libcst_equals() -> None:
    """Test arborista.parsers.python.equals_parser.LibcstEquals."""
    assert LibcstEquals == libcst.Equal


def test_inheritance() -> None:
    """Test arborista.parsers.python.equals_parser.EqualsParser inheritance."""
    assert issubclass(EqualsParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_equals, expected_equals', [
    (libcst.Equal(), Equals()),
])
# yapf: enable
def test_parse_equals(libcst_equals: LibcstEquals, expected_equals: Equals) -> None:
    """Test arborista.parsers.python.equals_parser.EqualsParser.parse_equals."""
    equals: Equals = EqualsParser.parse_equals(libcst_equals)

    assert equals == expected_equals
