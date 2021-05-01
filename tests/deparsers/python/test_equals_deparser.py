"""Test arborista.deparsers.python.equals_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.equals_deparser import EqualsDeparser
from arborista.nodes.python.equals import Equals


def test_inheritance() -> None:
    """Test arborista.deparsers.python.equals_deparser.EqualsDeparser inheritance."""
    assert issubclass(EqualsDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('equals, expected_string', [
    (Equals(), '=='),
])
# yapf: enable
def test_deparse_equals(equals: Equals, expected_string: str) -> None:
    """Test arborista.deparsers.python.equals_deparser.EqualsDeparser.deparse_equals."""
    string: str = EqualsDeparser.deparse_equals(equals)

    assert string == expected_string
