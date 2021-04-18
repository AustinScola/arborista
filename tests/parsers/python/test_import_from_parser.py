"""Test arborista.parsers.python.import_from_parser."""
from typing import Union

import libcst
import pytest

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.import_from import ImportFrom
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.relative_dotted_name import RelativeDottedName
from arborista.nodes.python.star import Star
from arborista.parser import Parser
from arborista.parsers.python.import_from_parser import (ImportFromParser, LibcstImportFrom, Source,
                                                         Target)


def test_libcst_import_from() -> None:
    """Test arborista.parsers.python.import_from_parser.LibcstImportFrom."""
    assert LibcstImportFrom == libcst.ImportFrom


def test_source() -> None:
    """Test arborista.parsers.python.import_from_parser.Source."""
    assert isinstance(Source, type(Union))
    assert Source.__args__ == (  # type: ignore[attr-defined]
        DottedName, RelativeDottedName)


def test_target() -> None:
    """Test arborista.parsers.python.import_from_parser.Target."""
    assert isinstance(Target, type(Union))
    assert Target.__args__ == (  # type: ignore[attr-defined]
        Star, GroupedNameAsNames, NameAsNames)


def test_inheritance() -> None:
    """Test arborista.parsers.python.import_from_parser.ImportFromParser inheritance."""
    assert issubclass(ImportFromParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_import_from, expected_import_from', [
    (libcst.ImportFrom(libcst.Name('foo'), [libcst.ImportAlias(libcst.Name('bar'))]), ImportFrom(DottedName(Name('foo'), []), NameAsNames(NameAsName(Name('bar', None)), []))),
    (libcst.ImportFrom(libcst.Name('foo'), [libcst.ImportAlias(libcst.Name('bar'))], lpar=libcst.LeftParen(), rpar=libcst.RightParen()), ImportFrom(DottedName(Name('foo'), []), GroupedNameAsNames(NameAsNames(NameAsName(Name('bar', None)), [])))),
    (libcst.ImportFrom(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), [libcst.ImportAlias(libcst.Name('baz'))]), ImportFrom(DottedName(Name('foo'), [Name('bar')]), NameAsNames(NameAsName(Name('baz', None)), []))),
    (libcst.ImportFrom(libcst.Name('foo'), libcst.ImportStar()), ImportFrom(DottedName(Name('foo'), []), Star())),
    (libcst.ImportFrom(None, [libcst.ImportAlias(libcst.Name('foo'))], [libcst.Dot()]), ImportFrom(RelativeDottedName(1, None), NameAsNames(NameAsName(Name('foo', None)), []))),
    (libcst.ImportFrom(libcst.Name('foo'), [libcst.ImportAlias(libcst.Name('bar'))], [libcst.Dot()]), ImportFrom(RelativeDottedName(1, DottedName(Name('foo'), [])), NameAsNames(NameAsName(Name('bar', None)), []))),
    (libcst.ImportFrom(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), [libcst.ImportAlias(libcst.Name('baz'))], [libcst.Dot()]), ImportFrom(RelativeDottedName(1, DottedName(Name('foo'), [Name('bar')])), NameAsNames(NameAsName(Name('baz', None)), []))),
    (libcst.ImportFrom(libcst.Name('foo'), [libcst.ImportAlias(libcst.Name('bar'))]), ImportFrom(DottedName(Name('foo'), []), NameAsNames(NameAsName(Name('bar', None)), []))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_import_from(libcst_import_from: LibcstImportFrom,
                           expected_import_from: ImportFrom) -> None:
    """Test arborista.parsers.python.import_from_parser.ImportFromParser.parse_import_from."""
    import_from: ImportFrom = ImportFromParser.parse_import_from(libcst_import_from)

    print(type(import_from.source), type(expected_import_from.source))
    assert import_from == expected_import_from
