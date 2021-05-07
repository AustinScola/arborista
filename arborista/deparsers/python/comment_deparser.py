"""Deparser for a comment."""
from arborista.deparser import Deparser
from arborista.nodes.python.comment import Comment


class CommentDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a comment."""
    @staticmethod
    def deparse_comment(comment: Comment) -> str:
        """Deparse a comment."""
        string: str = comment.value
        return string
