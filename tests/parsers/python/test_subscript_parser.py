"""Test arborista.parsers.python.subscript_parser."""
import libcst
import pytest

from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.slice import Slice
from arborista.nodes.python.subscript import Subscript
from arborista.parser import Parser
from arborista.parsers.python.subscript_parser import LibcstSubscript, SubscriptParser


def test_libcst_subscript() -> None:
    """Test arborista.parsers.python.subscript_parser.LibcstSubscript."""
    assert LibcstSubscript == libcst.SubscriptElement


def test_inheritance() -> None:
    """Test arborista.parsers.python.subscript_parser.SubscriptParser inheritance."""
    assert issubclass(SubscriptParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_subscript, expected_subscript', [
    (libcst.SubscriptElement(libcst.Index(libcst.Integer('0'))), Index(Integer(0))),
    (libcst.SubscriptElement(libcst.Slice(libcst.Integer('0'), libcst.Integer('1'))), Slice(Integer(0), Integer(1), None)),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_subscript(libcst_subscript: LibcstSubscript, expected_subscript: Subscript) -> None:
    """Test arborista.parsers.python.subscript_parser.SubscriptParser.parse_subscript."""
    subscript: Subscript = SubscriptParser.parse_subscript(libcst_subscript)

    assert subscript == expected_subscript
