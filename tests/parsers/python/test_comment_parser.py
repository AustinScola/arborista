"""Test arborista.parsers.python.comment_parser."""
import libcst
import pytest

from arborista.nodes.python.comment import Comment
from arborista.parser import Parser
from arborista.parsers.python.comment_parser import CommentParser, LibcstComment


def test_libcst_comment() -> None:
    """Test arborista.parsers.python.comment_parser.LibcstComment."""
    assert LibcstComment == libcst.Comment


def test_inheritance() -> None:
    """Test arborista.parsers.python.comment_parser.CommentParser inheritance."""
    assert issubclass(CommentParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_comment, expected_comment', [
    (libcst.Comment('# foo'), Comment('# foo')),
])
# yapf: enable
def test_parse_comment(libcst_comment: LibcstComment, expected_comment: Comment) -> None:
    """Test arborista.parsers.python.comment_parser.CommentParser.parse_comment."""  # pylint: disable=line-too-long, useless-suppression
    comment: Comment = CommentParser.parse_comment(libcst_comment)

    assert comment == expected_comment
