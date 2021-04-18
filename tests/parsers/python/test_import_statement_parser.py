"""Test arborista.parsers.python.import_statement_parser."""
from typing import Union

import libcst
import pytest

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.nodes.python.import_from import ImportFrom
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.parser import Parser
from arborista.parsers.python.import_statement_parser import (ImportStatementParser,
                                                              LibcstImportStatement)


def test_libcst_import_statement() -> None:
    """Test arborista.parsers.python.import_statement_parser.LibcstImportStatement."""
    assert isinstance(LibcstImportStatement, type(Union))
    assert LibcstImportStatement.__args__ == (  # type: ignore[attr-defined]
        libcst.Import, libcst.ImportFrom)


def test_inheritance() -> None:
    """Test arborista.parsers.python.import_statement_parser.ImportStatementParser inheritance."""
    assert issubclass(ImportStatementParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_import_statement, expected_import_statement', [
    (libcst.Import([libcst.ImportAlias(libcst.Name('foo'))]), ImportDottedName(DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), []))),
    (libcst.Import([libcst.ImportAlias(libcst.Name('foo'), libcst.AsName(libcst.Name('bar')))]), ImportDottedName(DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), Name('bar')), []))),
    (libcst.ImportFrom(libcst.Name('foo'), [libcst.ImportAlias(libcst.Name('bar'))]), ImportFrom(DottedName(Name('foo'), []), NameAsNames(NameAsName(Name('bar', None)), []))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_import_statement(libcst_import_statement: LibcstImportStatement,
                                expected_import_statement: ImportStatement) -> None:
    """Test arborista.parsers.python.import_statement_parser.ImportStatementParser.parse_import_statement."""  # pylint: disable=line-too-long, useless-suppression
    import_statement: ImportStatement = ImportStatementParser.parse_import_statement(
        libcst_import_statement)

    assert import_statement == expected_import_statement
