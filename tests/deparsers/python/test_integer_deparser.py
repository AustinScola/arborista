"""Test arborista.deparsers.python.integer_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.integer_deparser import IntegerDeparser
from arborista.nodes.python.integer import Integer


def test_inheritance() -> None:
    """Test arborista.deparsers.python.integer_deparser.IntegerDeparser inheritance."""
    assert issubclass(IntegerDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('integer, expected_string', [
    (Integer(1), '1'),
])
# yapf: enable
def test_deparse_integer(integer: Integer, expected_string: str) -> None:
    """Test arborista.deparsers.python.integer_deparser.IntegerDeparser.deparse_integer."""
    string: str = IntegerDeparser.deparse_integer(integer)

    assert string == expected_string
