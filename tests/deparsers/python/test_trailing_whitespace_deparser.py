"""Test arborista.deparsers.python.trailing_whitespace_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.trailing_whitespace_deparser import TrailingWhitespaceDeparser
from arborista.nodes.python.comment import Comment
from arborista.nodes.python.newline import Newline
from arborista.nodes.python.simple_whitespace import SimpleWhitespace
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace


def test_inheritance() -> None:
    """Test arborista.deparsers.python.trailing_whitespace_deparser.TrailingWhitespaceDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(TrailingWhitespaceDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('trailing_whitespace, expected_string', [
    (TrailingWhitespace(), '\n'),
    (TrailingWhitespace(SimpleWhitespace(' ')), ' \n'),
    (TrailingWhitespace(SimpleWhitespace('\t')), '\t\n'),
    (TrailingWhitespace(comment=Comment('# foo')), '# foo\n'),
    (TrailingWhitespace(newline=Newline('\r\n')), '\r\n'),
    (TrailingWhitespace(SimpleWhitespace(' '), Comment('# foo'), Newline('\r\n')), ' # foo\r\n'),
])
# yapf: enable
def test_deparse_trailing_whitespace(trailing_whitespace: TrailingWhitespace,
                                     expected_string: str) -> None:
    """Test arborista.deparsers.python.trailing_whitespace_deparser.TrailingWhitespaceDeparser.deparse_trailing_whitespace."""  # pylint: disable=line-too-long, useless-suppression
    string: str = TrailingWhitespaceDeparser.deparse_trailing_whitespace(trailing_whitespace)

    assert string == expected_string
