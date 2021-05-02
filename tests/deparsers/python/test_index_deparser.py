"""Test arborista.deparsers.python.index_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.index_deparser import IndexDeparser
from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer


def test_inheritance() -> None:
    """Test arborista.deparsers.python.index_deparser.IndexDeparser inheritance."""
    assert issubclass(IndexDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('index, expected_string', [
    (Index(Integer(0)), '0'),
])
# yapf: enable
def test_deparse_index(index: Index, expected_string: str) -> None:
    """Test arborista.deparsers.python.index_deparser.IndexDeparser.deparse_index."""
    string: str = IndexDeparser.deparse_index(index)

    assert string == expected_string
