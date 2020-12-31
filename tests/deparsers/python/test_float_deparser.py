"""Test arborista.deparsers.python.float_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.float_deparser import FloatDeparser
from arborista.nodes.python.float import Float


def test_inheritance() -> None:
    """Test arborista.deparsers.python.float_deparser.FloatDeparser inheritance."""
    assert issubclass(FloatDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('float_, expected_string', [
    (Float(1.0), '1.0'),
])
# yapf: enable
def test_deparse_float(float_: Float, expected_string: str) -> None:
    """Test arborista.deparsers.python.float_deparser.FloatDeparser.deparse_float."""
    string: str = FloatDeparser.deparse_float(float_)

    assert string == expected_string
