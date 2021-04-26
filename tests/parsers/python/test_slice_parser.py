"""Test arborista.parsers.python.slice_parser."""
import libcst
import pytest

from arborista.nodes.python.name import Name
from arborista.nodes.python.slice import Slice
from arborista.parser import Parser
from arborista.parsers.python.slice_parser import LibcstSlice, SliceParser


def test_libcst_slice() -> None:
    """Test arborista.parsers.python.slice_parser.LibcstSlice."""
    assert LibcstSlice == libcst.Slice


def test_inheritance() -> None:
    """Test arborista.parsers.python.slice_parser.SliceParser inheritance."""
    assert issubclass(SliceParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_slice, expected_slice', [
    (libcst.Slice(None, None), Slice(None, None, None)),
    (libcst.Slice(libcst.Name('foo'), libcst.Name('bar'), libcst.Name('baz')), Slice(Name('foo'), Name('bar'), Name('baz'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_slice(libcst_slice: LibcstSlice, expected_slice: Slice) -> None:
    """Test arborista.parsers.python.slice_parser.SliceParser.parse_slice."""
    slice_: Slice = SliceParser.parse_slice(libcst_slice)

    assert slice_ == expected_slice
