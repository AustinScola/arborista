"""Test arborista.parsers.python.imaginary_parser."""
import libcst
import pytest

from arborista.nodes.python.imaginary import Imaginary
from arborista.parser import Parser
from arborista.parsers.python.imaginary_parser import ImaginaryParser, LibcstImaginary


def test_inheritance() -> None:
    """Test arborista.parsers.python.imaginary_parser.ImaginaryParser inheritance."""
    assert issubclass(ImaginaryParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_imaginary, expected_imaginary', [
    (libcst.Imaginary('1j'), Imaginary(1)),
    (libcst.Imaginary('1.0j'), Imaginary(1.0)),
])
# yapf: enable
def test_parse_imaginary(libcst_imaginary: LibcstImaginary, expected_imaginary: Imaginary) -> None:
    """Test arborista.parsers.python.imaginary_parser.ImaginaryParser.parse_imaginary."""
    imaginary: Imaginary = ImaginaryParser.parse_imaginary(libcst_imaginary)

    assert imaginary == expected_imaginary
