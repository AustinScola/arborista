"""Test arborista.deparsers.python.name_as_names_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.name_as_names_deparser import NameAsNamesDeparser
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames


def test_inheritance() -> None:
    """Test arborista.deparsers.python.name_as_names_deparser.NameAsNamesDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(NameAsNamesDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('name_as_names, expected_string', [
    (NameAsNames(NameAsName(Name('foo'), None), []), 'foo'),
    (NameAsNames(NameAsName(Name('foo'), None), [NameAsName(Name('bar'), None)]), 'foo, bar'),
    (NameAsNames(NameAsName(Name('foo'), None), [NameAsName(Name('bar'), None), NameAsName(Name('baz'), None)]), 'foo, bar, baz'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_name_as_names(name_as_names: NameAsNames, expected_string: str) -> None:
    """Test arborista.deparsers.python.name_as_names_deparser.NameAsNamesDeparser.deparse_name_as_names."""  # pylint: disable=line-too-long, useless-suppression
    string: str = NameAsNamesDeparser.deparse_name_as_names(name_as_names)

    assert string == expected_string
