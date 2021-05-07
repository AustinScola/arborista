"""Parser for comment."""
import libcst

from arborista.nodes.python.comment import Comment
from arborista.parser import Parser

LibcstComment = libcst.Comment


class CommentParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for comment."""
    @staticmethod
    def parse_comment(libcst_comment: LibcstComment) -> Comment:
        """Parse comment."""
        value: str = libcst_comment.value

        comment: Comment = Comment(value)

        return comment
