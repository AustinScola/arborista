"""Test arborista.deparsers.python.import_from_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.import_from_deparser import ImportFromDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.import_from import ImportFrom
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.relative_dotted_name import RelativeDottedName
from arborista.nodes.python.star import Star


def test_inheritance() -> None:
    """Test arborista.deparsers.python.import_from_deparser.ImportFromDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ImportFromDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('import_from, expected_string', [
    (ImportFrom(DottedName(Name('foo'), []), NameAsNames(NameAsName(Name('bar', None)), [])), 'from foo import bar'),
    (ImportFrom(RelativeDottedName(1, DottedName(Name('foo'), [])), NameAsNames(NameAsName(Name('bar'), None), [])), 'from .foo import bar'),
    (ImportFrom(DottedName(Name('foo'), []), GroupedNameAsNames(NameAsNames(NameAsName(Name('bar'), None), []))), 'from foo import (bar)'),
    (ImportFrom(DottedName(Name('foo'), []), Star()), 'from foo import *'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_import_from(import_from: ImportFrom, expected_string: str) -> None:
    """Test arborista.deparsers.python.import_from_deparser.ImportFromDeparser.deparse_import_from."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ImportFromDeparser.deparse_import_from(import_from)

    assert string == expected_string
