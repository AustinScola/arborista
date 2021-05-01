"""Test arborista.deparsers.python.comparison_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.comparison_deparser import ComparisonDeparser
from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.equals import Equals
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.comparison_deparser.ComparisonDeparser inheritance."""
    assert issubclass(ComparisonDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('comparison, expected_string', [
    (Comparison(Name('foo'), Equals(), Name('bar')), 'foo == bar'),
])
# yapf: enable
def test_deparse_comparison(comparison: Comparison, expected_string: str) -> None:
    """Test arborista.deparsers.python.comparison_deparser.ComparisonDeparser.deparse_comparison."""
    string: str = ComparisonDeparser.deparse_comparison(comparison)

    assert string == expected_string
