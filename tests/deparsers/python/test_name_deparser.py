"""Test arborista.deparsers.python.name_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.name_deparser.NameDeparser inheritance."""
    assert issubclass(NameDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('name, expected_string', [
    (Name('foo'), 'foo'),
])
# yapf: enable
def test_deparse_name(name: Name, expected_string: str) -> None:
    """Test arborista.deparsers.python.name_deparser.NameDeparser.deparse_name."""
    string: str = NameDeparser.deparse_name(name)
    assert string == expected_string
