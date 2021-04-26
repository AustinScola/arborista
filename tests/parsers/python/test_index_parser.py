"""Test arborista.parsers.python.index_parser."""
import libcst
import pytest

from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.parser import Parser
from arborista.parsers.python.index_parser import IndexParser, LibcstIndex


def test_libcst_index() -> None:
    """Test arborista.parsers.python.index_parser.LibcstIndex."""
    assert LibcstIndex == libcst.Index


def test_inheritance() -> None:
    """Test arborista.parsers.python.index_parser.IndexParser inheritance."""
    assert issubclass(IndexParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_index, expected_index', [
    (libcst.Index(libcst.Integer('0')), Index(Integer(0))),
])
# yapf: enable
def test_parse_index(libcst_index: LibcstIndex, expected_index: Index) -> None:
    """Test arborista.parsers.python.index_parser.IndexParser.parse_index."""
    index: Index = IndexParser.parse_index(libcst_index)

    assert index == expected_index
