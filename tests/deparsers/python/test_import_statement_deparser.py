"""Test arborista.deparsers.python.import_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.import_statement_deparser import ImportStatementDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.nodes.python.import_from import ImportFrom
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames


def test_inheritance() -> None:
    """Test arborista.deparsers.python.import_statement_deparser.ImportStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ImportStatementDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('import_statement, expected_string', [
    (ImportDottedName(DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), [])), 'import foo'),
    (ImportFrom(DottedName(Name('foo'), []), NameAsNames(NameAsName(Name('bar', None)), [])), 'from foo import bar'),

])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_import_statement(import_statement: ImportStatement, expected_string: str) -> None:
    """Test arborista.deparsers.python.import_statement_deparser.ImportStatementDeparser.deparse_import_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ImportStatementDeparser.deparse_import_statement(import_statement)

    assert string == expected_string
