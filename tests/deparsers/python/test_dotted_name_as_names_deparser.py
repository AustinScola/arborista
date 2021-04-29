"""Test arborista.deparsers.python.dotted_name_as_names_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.dotted_name_as_names_deparser import DottedNameAsNamesDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.dotted_name_as_names_deparser.DottedNameAsNamesDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(DottedNameAsNamesDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('dotted_name_as_names, expected_string', [
    (DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), []), 'foo'),
    (DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), [DottedNameAsName(DottedName(Name('bar'), []), None)]), 'foo, bar'),
    (DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), [DottedNameAsName(DottedName(Name('bar'), []), None), DottedNameAsName(DottedName(Name('baz'), []), None)]), 'foo, bar, baz'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_dotted_name_as_names(dotted_name_as_names: DottedNameAsNames,
                                      expected_string: str) -> None:
    """Test arborista.deparsers.python.dotted_name_as_names_deparser.DottedNameAsNamesDeparser.deparse_dotted_name_as_names."""  # pylint: disable=line-too-long, useless-suppression
    string: str = DottedNameAsNamesDeparser.deparse_dotted_name_as_names(dotted_name_as_names)

    assert string == expected_string
