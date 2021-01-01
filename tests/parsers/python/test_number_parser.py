"""Test arborista.parsers.python.number_parser."""
import libcst
import pytest

from arborista.nodes.python.float import Float
from arborista.nodes.python.imaginary import Imaginary
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.number import Number
from arborista.parser import Parser
from arborista.parsers.python.number_parser import LibcstNumber, NumberParser


def test_inheritance() -> None:
    """Test arborista.parsers.python.number_parser.NumberParser inheritance."""
    assert issubclass(NumberParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_number, expected_number', [
    (libcst.Integer('1'), Integer(1)),
    (libcst.Float('1.0'), Float(1.0)),
    (libcst.Imaginary('1.0j'), Imaginary(1.0)),
])
# yapf: enable
def test_parse_number(libcst_number: LibcstNumber, expected_number: Number) -> None:
    """Test arborista.parsers.python.number_parser.NumberParser.parse_number."""
    number: Number = NumberParser.parse_number(libcst_number)

    assert number == expected_number
