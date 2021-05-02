"""Test arborista.deparsers.python.subscript_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.subscript_deparser import SubscriptDeparser
from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.slice import Slice
from arborista.nodes.python.subscript import Subscript


def test_inheritance() -> None:
    """Test arborista.deparsers.python.subscript_deparser.SubscriptDeparser inheritance."""
    assert issubclass(SubscriptDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('subscript, expected_string', [
    (Index(Integer(0)), '0'),
    (Slice(Integer(0), Integer(1), Integer(-1)), '0:1:-1'),
])
# yapf: enable
def test_deparse_subscript(subscript: Subscript, expected_string: str) -> None:
    """Test arborista.deparsers.python.subscript_deparser.SubscriptDeparser.deparse_subscript."""
    string: str = SubscriptDeparser.deparse_subscript(subscript)

    assert string == expected_string
