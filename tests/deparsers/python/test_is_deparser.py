"""Test arborista.deparsers.python.is_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.is_deparser import IsDeparser
from arborista.nodes.python.is_ import Is


def test_inheritance() -> None:
    """Test arborista.deparsers.python.is_deparser.IsDeparser inheritance."""
    assert issubclass(IsDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('is_, expected_string', [
    (Is(), 'is'),
])
# yapf: enable
def test_deparse_is_(is_: Is, expected_string: str) -> None:
    """Test arborista.deparsers.python.is_deparser.IsDeparser.deparse_is."""
    string: str = IsDeparser.deparse_is(is_)

    assert string == expected_string
