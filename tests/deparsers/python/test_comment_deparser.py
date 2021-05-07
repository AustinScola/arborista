"""Test arborista.deparsers.python.comment_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.comment_deparser import CommentDeparser
from arborista.nodes.python.comment import Comment


def test_inheritance() -> None:
    """Test arborista.deparsers.python.comment_deparser.CommentDeparser inheritance."""
    assert issubclass(CommentDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('comment, expected_string', [
    (Comment('# foo'), '# foo'),
])
# yapf: enable
def test_deparse_comment(comment: Comment, expected_string: str) -> None:
    """Test arborista.deparsers.python.comment_deparser.CommentDeparser.deparse_comment."""
    string: str = CommentDeparser.deparse_comment(comment)

    assert string == expected_string
