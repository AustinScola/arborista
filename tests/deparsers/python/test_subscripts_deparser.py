"""Test arborista.deparsers.python.subscripts_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.subscripts_deparser import SubscriptsDeparser
from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.subscripts import Subscripts


def test_inheritance() -> None:
    """Test arborista.deparsers.python.subscripts_deparser.SubscriptsDeparser inheritance."""
    assert issubclass(SubscriptsDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('subscripts, expected_string', [
    (Subscripts(Index(Integer(0)), []), '0'),
    (Subscripts(Index(Integer(0)), [Index(Integer(1))]), '0, 1'),
    (Subscripts(Index(Integer(0)), [Index(Integer(1)), Index(Integer(2))]), '0, 1, 2'),
])
# yapf: enable
def test_deparse_subscripts(subscripts: Subscripts, expected_string: str) -> None:
    """Test arborista.deparsers.python.subscripts_deparser.SubscriptsDeparser.deparse_subscripts."""
    string: str = SubscriptsDeparser.deparse_subscripts(subscripts)

    assert string == expected_string
