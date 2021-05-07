"""Test arborista.parsers.python.newline_parser."""
import libcst
import pytest

from arborista.nodes.python.newline import Newline
from arborista.parser import Parser
from arborista.parsers.python.newline_parser import LibcstNewline, NewlineParser


def test_libcst_newline() -> None:
    """Test arborista.parsers.python.newline_parser.LibcstNewline."""
    assert LibcstNewline == libcst.Newline


def test_inheritance() -> None:
    """Test arborista.parsers.python.newline_parser.NewlineParser inheritance."""
    assert issubclass(NewlineParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_newline, expected_newline', [
    (libcst.Newline(), Newline()),
    (libcst.Newline('\n'), Newline('\n')),
    (libcst.Newline('\r\n'), Newline('\r\n')),
])
# yapf: enable
def test_parse_newline(libcst_newline: LibcstNewline, expected_newline: Newline) -> None:
    """Test arborista.parsers.python.newline_parser.NewlineParser.parse_newline."""  # pylint: disable=line-too-long, useless-suppression
    newline: Newline = NewlineParser.parse_newline(libcst_newline)

    assert newline == expected_newline
