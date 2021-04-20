"""Test arborista.parsers.python.comparison_parser."""
import libcst
import pytest

from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.equals import Equals
from arborista.nodes.python.integer import Integer
from arborista.parser import Parser
from arborista.parsers.python.comparison_parser import ComparisonParser, LibcstComparison


def test_libcst_comparison() -> None:
    """Test arborista.parsers.python.comparison_parser.LibcstComparison."""
    assert LibcstComparison == libcst.Comparison


def test_inheritance() -> None:
    """Test arborista.parsers.python.comparison_parser.ComparisonParser inheritance."""
    assert issubclass(ComparisonParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_comparison, expected_comparison', [
    (libcst.Comparison(libcst.Integer('1'), [libcst.ComparisonTarget(libcst.Equal(), libcst.Integer('2'))]), Comparison(Integer(1), Equals(), Integer(2))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_comparison(libcst_comparison: LibcstComparison,
                          expected_comparison: Comparison) -> None:
    """Test arborista.parsers.python.comparison_parser.ComparisonParser.parse_comparison."""
    comparison: Comparison = ComparisonParser.parse_comparison(libcst_comparison)

    assert comparison == expected_comparison
