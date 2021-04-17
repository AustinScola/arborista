"""Test arborista.parsers.python.import_dotted_name_parser."""
import libcst
import pytest

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.import_dotted_name_parser import (ImportDottedNameParser,
                                                                LibcstImportDottedName)


def test_libcst_import_dotted_name() -> None:
    """Test arborista.parsers.python.import_dotted_name_parser.LibcstImportDottedName."""
    assert LibcstImportDottedName == libcst.Import


def test_inheritance() -> None:
    """Test arborista.parsers.python.import_dotted_name_parser.ImportDottedNameParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ImportDottedNameParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_import_dotted_name, expected_import_dotted_name', [
    (libcst.Import([libcst.ImportAlias(libcst.Name('foo'))]), ImportDottedName(DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), []))),
    (libcst.Import([libcst.ImportAlias(libcst.Name('foo'), libcst.AsName(libcst.Name('bar')))]), ImportDottedName(DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), Name('bar')), []))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_import_dotted_name(libcst_import_dotted_name: LibcstImportDottedName,
                                  expected_import_dotted_name: ImportDottedName) -> None:
    """Test arborista.parsers.python.import_dotted_name_parser.ImportDottedNameParser.parse_import_dotted_name."""  # pylint: disable=line-too-long, useless-suppression
    import_dotted_name: ImportDottedName = ImportDottedNameParser.parse_import_dotted_name(
        libcst_import_dotted_name)

    assert import_dotted_name == expected_import_dotted_name
