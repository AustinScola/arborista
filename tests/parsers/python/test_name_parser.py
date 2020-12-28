"""Test arborista.parsers.python.name_parser."""
import libcst
import pytest

from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.name_parser import LibcstName, NameParser


def test_inheritance() -> None:
    """Test arborista.parsers.python.name_parser.NameParser inheritance."""
    assert issubclass(NameParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_name, expected_name', [
    (libcst.Name('foo'), Name('foo')),
])
# yapf: enable
def test_parse_name(libcst_name: LibcstName, expected_name: Name) -> None:
    """Test arborista.parsers.python.name_parser.NameParser.parse_name."""
    name: Name = NameParser.parse_name(libcst_name)

    assert name == expected_name
