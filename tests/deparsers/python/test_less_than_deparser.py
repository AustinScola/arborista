"""Test arborista.deparsers.python.less_than_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.less_than_deparser import LessThanDeparser
from arborista.nodes.python.less_than import LessThan


def test_inheritance() -> None:
    """Test arborista.deparsers.python.less_than_deparser.LessThanDeparser inheritance."""
    assert issubclass(LessThanDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('less_than, expected_string', [
    (LessThan(), '<'),
])
# yapf: enable
def test_deparse_less_than(less_than: LessThan, expected_string: str) -> None:
    """Test arborista.deparsers.python.less_than_deparser.LessThanDeparser.deparse_less_than."""
    string: str = LessThanDeparser.deparse_less_than(less_than)

    assert string == expected_string
