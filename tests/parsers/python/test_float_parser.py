"""Test arborista.parsers.python.float_parser."""
import libcst
import pytest

from arborista.nodes.python.float import Float
from arborista.parser import Parser
from arborista.parsers.python.float_parser import FloatParser, LibcstFloat


def test_inheritance() -> None:
    """Test arborista.parsers.python.float_parser.FloatParser inheritance."""
    assert issubclass(FloatParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_float, expected_float', [
    (libcst.Float('1.0'), Float(1.0)),
])
# yapf: enable
def test_parse_float(libcst_float: LibcstFloat, expected_float: Float) -> None:
    """Test arborista.parsers.python.float_parser.FloatParser.parse_float."""
    float_: Float = FloatParser.parse_float(libcst_float)

    assert float_ == expected_float
