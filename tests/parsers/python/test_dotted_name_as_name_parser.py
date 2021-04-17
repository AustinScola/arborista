"""Test arborista.parsers.python.dotted_name_as_name_parser."""
import libcst
import pytest

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.dotted_name_as_name_parser import (DottedNameAsNameParser,
                                                                 LibcstDottedNameAsName)


def test_libcst_dotted_name_as_name() -> None:
    """Test arborista.parsers.python.dotted_name_as_name_parser.LibcstDottedNameAsNamei."""
    assert LibcstDottedNameAsName == libcst.ImportAlias


def test_inheritance() -> None:
    """Test arborista.parsers.python.dotted_name_as_name_parser.DottedNameAsNameParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(DottedNameAsNameParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_dotted_name_as_name, expected_dotted_name_as_name', [
    (libcst.ImportAlias(libcst.Name('foo')), DottedNameAsName(DottedName(Name('foo'), []), None)),
    (libcst.ImportAlias(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar'))), DottedNameAsName(DottedName(Name('foo'), [Name('bar')]), None)),
    (libcst.ImportAlias(libcst.Attribute(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), libcst.Name('baz'))), DottedNameAsName(DottedName(Name('foo'), [Name('bar'), Name('baz')]), None)),
    (libcst.ImportAlias(libcst.Name('foo'), libcst.AsName(libcst.Name('bar'))), DottedNameAsName(DottedName(Name('foo'), []), Name('bar'))),
    (libcst.ImportAlias(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), libcst.AsName(libcst.Name('baz'))), DottedNameAsName(DottedName(Name('foo'), [Name('bar')]), Name('baz'))),
    (libcst.ImportAlias(libcst.Attribute(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), libcst.Name('baz')), libcst.AsName(libcst.Name('wibble'))), DottedNameAsName(DottedName(Name('foo'), [Name('bar'), Name('baz')]), Name('wibble'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_dotted_name_as_name(libcst_dotted_name_as_name: LibcstDottedNameAsName,
                                   expected_dotted_name_as_name: DottedNameAsName) -> None:
    """Test arborista.parsers.python.dotted_name_as_name_parser.DottedNameAsNameParser.parse_dotted_name_as_name."""  # pylint: disable=line-too-long, useless-suppression
    dotted_name_as_name: DottedNameAsName = DottedNameAsNameParser.parse_dotted_name_as_name(
        libcst_dotted_name_as_name)

    assert dotted_name_as_name == expected_dotted_name_as_name
