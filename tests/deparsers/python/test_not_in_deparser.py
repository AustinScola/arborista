"""Test arborista.deparsers.python.not_in_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.not_in_deparser import NotInDeparser
from arborista.nodes.python.not_in import NotIn


def test_not_inheritance() -> None:
    """Test arborista.deparsers.python.not_in_deparser.NotInDeparser not_inheritance."""
    assert issubclass(NotInDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('not_in_, expected_strnot_ing', [
    (NotIn(), 'not in'),
])
# yapf: enable
def test_deparse_not_in_(not_in_: NotIn, expected_strnot_ing: str) -> None:
    """Test arborista.deparsers.python.not_in_deparser.NotInDeparser.deparse_not_in."""
    strnot_ing: str = NotInDeparser.deparse_not_in(not_in_)

    assert strnot_ing == expected_strnot_ing
