"""Test arborista.deparsers.python.star_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.star_deparser import StarDeparser
from arborista.nodes.python.star import Star


def test_inheritance() -> None:
    """Test arborista.deparsers.python.star_deparser.StarDeparser inheritance."""
    assert issubclass(StarDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('star, expected_string', [
    (Star(), '*'),
])
# yapf: enable
def test_deparse_star(star: Star, expected_string: str) -> None:
    """Test arborista.deparsers.python.star_deparser.StarDeparser.deparse_star."""
    string: str = StarDeparser.deparse_star(star)

    assert string == expected_string
