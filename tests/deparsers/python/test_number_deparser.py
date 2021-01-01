"""Test arborista.deparsers.python.number_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.number_deparser import NumberDeparser
from arborista.nodes.python.float import Float
from arborista.nodes.python.imaginary import Imaginary
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.number import Number


def test_inheritance() -> None:
    """Test arborista.deparsers.python.number_deparser.NumberDeparser inheritance."""
    assert issubclass(NumberDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('number, expected_string', [
    (Integer(1), '1'),
    (Float(1.0), '1.0'),
    (Imaginary(1), '1j'),
])
# yapf: enable
def test_deparse_number(number: Number, expected_string: str) -> None:
    """Test arborista.deparsers.python.number_deparser.NumberDeparser.deparse_number."""
    string: str = NumberDeparser.deparse_number(number)

    assert string == expected_string
