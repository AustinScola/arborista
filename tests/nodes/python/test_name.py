"""Test arborista.nodes.python.name."""
import pytest

from arborista.nodes.python.name import Name


# yapf: disable
@pytest.mark.parametrize('value', [
    ('f'),
])
# yapf: enable
def test_init(value: str) -> None:
    """Test arborista.nodes.python.name.__init__."""
    name: Name = Name(value)

    assert name.value == value
