"""Test arborista.parsers.python.empty_line_parser."""
import libcst
import pytest

from arborista.nodes.python.empty_line import EmptyLine
from arborista.parser import Parser
from arborista.parsers.python.empty_line_parser import EmptyLineParser, LibcstEmptyLine


def test_libcst_empty_line() -> None:
    """Test arborista.parsers.python.empty_line_parser.LibcstEmptyLine."""
    assert LibcstEmptyLine == libcst.EmptyLine


def test_inheritance() -> None:
    """Test arborista.parsers.python.empty_line_parser.EmptyLineParser inheritance."""
    assert issubclass(EmptyLineParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_empty_line, expected_empty_line', [
    (libcst.EmptyLine(), EmptyLine()),
])
# yapf: enable
def test_parse_empty_line(libcst_empty_line: LibcstEmptyLine,
                          expected_empty_line: EmptyLine) -> None:
    """Test arborista.parsers.python.empty_line_parser.EmptyLineParser.parse_empty_line."""
    empty_line: EmptyLine = EmptyLineParser.parse_empty_line(libcst_empty_line)

    assert empty_line == expected_empty_line
