"""Deparser for trailing whitespace."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.comment_deparser import CommentDeparser
from arborista.deparsers.python.newline_deparser import NewlineDeparser
from arborista.deparsers.python.simple_whitespace_deparser import SimpleWhitespaceDeparser
from arborista.nodes.python.comment import Comment
from arborista.nodes.python.newline import Newline
from arborista.nodes.python.simple_whitespace import SimpleWhitespace
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace


class TrailingWhitespaceDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for trailing whitespace."""
    @staticmethod
    def deparse_trailing_whitespace(trailing_whitespace: TrailingWhitespace) -> str:
        """Deparse trailing whitespace."""
        string: str = ''

        whitespace: Optional[SimpleWhitespace] = trailing_whitespace.whitespace
        if whitespace is not None:
            whitespace_string: str = SimpleWhitespaceDeparser.deparse_simple_whitespace(whitespace)
            string += whitespace_string

        comment: Optional[Comment] = trailing_whitespace.comment
        if comment is not None:
            comment_string = CommentDeparser.deparse_comment(comment)
            string += comment_string

        newline: Newline = trailing_whitespace.newline
        newline_string = NewlineDeparser.deparse_newline(newline)
        string += newline_string

        return string
