"""Test arborista.deparsers.python.import_dotted_name_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.import_dotted_name_deparser import ImportDottedNameDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.import_dotted_name_deparser.ImportDottedNameDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ImportDottedNameDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('import_dotted_name, expected_string', [
    (ImportDottedName(DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), [])), [])), 'import foo'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_import_dotted_name(import_dotted_name: ImportDottedName,
                                    expected_string: str) -> None:
    """Test arborista.deparsers.python.import_dotted_name_deparser.ImportDottedNameDeparser.deparse_import_dotted_name."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ImportDottedNameDeparser.deparse_import_dotted_name(import_dotted_name)

    assert string == expected_string
