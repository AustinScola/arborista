"""Test arborista.deparsers.python.slice_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.slice_deparser import SliceDeparser
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.slice import Slice


def test_inheritance() -> None:
    """Test arborista.deparsers.python.slice_deparser.SliceDeparser inheritance."""
    assert issubclass(SliceDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('slice_, expected_string', [
    (Slice(None, None, None), ':'),
    (Slice(Integer(0), None, None), '0:'),
    (Slice(None, Integer(1), None), ':1'),
    (Slice(None, None, Integer(2)), '::2'),
    (Slice(Integer(0), Integer(1), Integer(-1)), '0:1:-1'),
])
# yapf: enable
def test_deparse_slice(slice_: Slice, expected_string: str) -> None:
    """Test arborista.deparsers.python.slice_deparser.SliceDeparser.deparse_slice_."""
    string: str = SliceDeparser.deparse_slice(slice_)

    assert string == expected_string
