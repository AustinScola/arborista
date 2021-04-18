"""Test arborista.parsers.python.name_as_name_parser."""
import libcst
import pytest

from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.parser import Parser
from arborista.parsers.python.name_as_name_parser import LibcstNameAsName, NameAsNameParser


def test_libcst_name_as_name() -> None:
    """Test arborista.parsers.python.name_as_name_parser.LibcstNameAsName."""
    assert LibcstNameAsName == libcst.ImportAlias


def test_inheritance() -> None:
    """Test arborista.parsers.python.name_as_name_parser.NameAsNameParser inheritance."""
    assert issubclass(NameAsNameParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_name_as_name, expected_name_as_name', [
    (libcst.ImportAlias(libcst.Name('foo')), NameAsName(Name('foo'), None)),
    (libcst.ImportAlias(libcst.Name('foo'), libcst.AsName(libcst.Name('bar'))), NameAsName(Name('foo'), Name('bar'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_name_as_name(libcst_name_as_name: LibcstNameAsName,
                            expected_name_as_name: NameAsName) -> None:
    """Test arborista.parsers.python.name_as_name_parser.NameAsNameParser.parse_name_as_name."""
    name_as_name: NameAsName = NameAsNameParser.parse_name_as_name(libcst_name_as_name)

    assert name_as_name == expected_name_as_name
