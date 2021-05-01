"""Test arborista.deparsers.python.in_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.in_deparser import InDeparser
from arborista.nodes.python.in_ import In


def test_inheritance() -> None:
    """Test arborista.deparsers.python.in_deparser.InDeparser inheritance."""
    assert issubclass(InDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('in_, expected_string', [
    (In(), 'in'),
])
# yapf: enable
def test_deparse_in_(in_: In, expected_string: str) -> None:
    """Test arborista.deparsers.python.in_deparser.InDeparser.deparse_in."""
    string: str = InDeparser.deparse_in(in_)

    assert string == expected_string
