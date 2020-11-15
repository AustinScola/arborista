"""Test arborista.nodes.python.name."""
import pytest

from arborista.nodes.python.atom import Atom
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.nodes.python.name.Name inheritance."""
    assert issubclass(Name, Atom)


# yapf: disable
@pytest.mark.parametrize('value', [
    ('f'),
])
# yapf: enable
def test_init(value: str) -> None:
    """Test arborista.nodes.python.name.__init__."""
    name: Name = Name(value)

    assert name.value == value
