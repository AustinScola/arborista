"""Test arborista.deparsers.python.imaginary_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.imaginary_deparser import ImaginaryDeparser
from arborista.nodes.python.imaginary import Imaginary


def test_inheritance() -> None:
    """Test arborista.deparsers.python.imaginary_deparser.ImaginaryDeparser inheritance."""
    assert issubclass(ImaginaryDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('imaginary, expected_string', [
    (Imaginary(1), '1j'),
    (Imaginary(1.0), '1.0j'),
])
# yapf: enable
def test_deparse_imaginary(imaginary: Imaginary, expected_string: str) -> None:
    """Test arborista.deparsers.python.imaginary_deparser.ImaginaryDeparser.deparse_imaginary."""
    string: str = ImaginaryDeparser.deparse_imaginary(imaginary)

    assert string == expected_string
