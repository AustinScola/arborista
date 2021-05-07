"""Test arborista.parsers.python.trailing_whitespace_parser."""
import libcst
import pytest

from arborista.nodes.python.comment import Comment
from arborista.nodes.python.newline import Newline
from arborista.nodes.python.simple_whitespace import SimpleWhitespace
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace
from arborista.parser import Parser
from arborista.parsers.python.trailing_whitespace_parser import (LibcstTrailingWhitespace,
                                                                 TrailingWhitespaceParser)


def test_libcst_trailing_whitespace() -> None:
    """Test arborista.parsers.python.trailing_whitespace_parser.LibcstTrailingWhitespace."""
    assert LibcstTrailingWhitespace == libcst.TrailingWhitespace


def test_inheritance() -> None:
    """Test arborista.parsers.python.trailing_whitespace_parser.TrailingWhitespaceParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(TrailingWhitespaceParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_trailing_whitespace, expected_trailing_whitespace', [
    (libcst.TrailingWhitespace(), TrailingWhitespace()),
    (libcst.TrailingWhitespace(libcst.SimpleWhitespace(' ')), TrailingWhitespace(SimpleWhitespace(' '))),
    (libcst.TrailingWhitespace(comment=libcst.Comment('# foo')), TrailingWhitespace(comment=Comment('# foo'))),
    (libcst.TrailingWhitespace(newline=libcst.Newline('\r\n')), TrailingWhitespace(newline=Newline('\r\n'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_trailing_whitespace(libcst_trailing_whitespace: LibcstTrailingWhitespace,
                                   expected_trailing_whitespace: TrailingWhitespace) -> None:
    """Test arborista.parsers.python.trailing_whitespace_parser.TrailingWhitespaceParser.parse_trailing_whitespace."""  # pylint: disable=line-too-long, useless-suppression
    trailing_whitespace: TrailingWhitespace = TrailingWhitespaceParser.parse_trailing_whitespace(
        libcst_trailing_whitespace)

    assert trailing_whitespace == expected_trailing_whitespace
