"""Test arborista.deparsers.python.name_as_name_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.name_as_name_deparser import NameAsNameDeparser
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName


def test_inheritance() -> None:
    """Test arborista.deparsers.python.name_as_name_deparser.NameAsNameDeparser inheritance."""
    assert issubclass(NameAsNameDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('name_as_name, expected_string', [
    (NameAsName(Name('foo'), None), 'foo'),
    (NameAsName(Name('foo'), Name('bar')), 'foo as bar'),
])
# yapf: enable
def test_deparse_name_as_name(name_as_name: NameAsName, expected_string: str) -> None:
    """Test arborista.deparsers.python.name_as_name_deparser.NameAsNameDeparser.deparse_name_as_name."""  # pylint: disable=line-too-long, useless-suppression
    string: str = NameAsNameDeparser.deparse_name_as_name(name_as_name)

    assert string == expected_string
