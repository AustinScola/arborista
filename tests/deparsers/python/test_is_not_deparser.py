"""Test arborista.deparsers.python.is_notdeparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.is_not_deparser import IsNotDeparser
from arborista.nodes.python.is_not import IsNot


def test_inheritance() -> None:
    """Test arborista.deparsers.python.is_notdeparser.IsNotDeparser inheritance."""
    assert issubclass(IsNotDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('is_not, expected_string', [
    (IsNot(), 'is not'),
])
# yapf: enable
def test_deparse_is_not(is_not: IsNot, expected_string: str) -> None:
    """Test arborista.deparsers.python.is_notdeparser.IsNotDeparser.deparse_is."""
    string: str = IsNotDeparser.deparse_is_not(is_not)

    assert string == expected_string
