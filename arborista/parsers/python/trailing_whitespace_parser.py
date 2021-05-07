"""Parser for trailing whitespace."""
from typing import Optional

import libcst

from arborista.nodes.python.comment import Comment
from arborista.nodes.python.newline import Newline
from arborista.nodes.python.simple_whitespace import SimpleWhitespace
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace
from arborista.parser import Parser
from arborista.parsers.python.comment_parser import CommentParser, LibcstComment
from arborista.parsers.python.newline_parser import LibcstNewline, NewlineParser
from arborista.parsers.python.simple_whitespace_parser import (LibcstSimpleWhitespace,
                                                               SimpleWhitespaceParser)

LibcstTrailingWhitespace = libcst.TrailingWhitespace


class TrailingWhitespaceParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for trailing whitespace."""
    @staticmethod
    def parse_trailing_whitespace(
            libcst_trailing_whitespace: LibcstTrailingWhitespace) -> TrailingWhitespace:
        """Parse trailing whitespace."""
        trailing_whitespace: TrailingWhitespace

        libcst_whitespace: LibcstSimpleWhitespace = libcst_trailing_whitespace.whitespace
        whitespace: Optional[SimpleWhitespace]
        if libcst_whitespace.value:
            whitespace = SimpleWhitespaceParser.parse_simple_whitespace(libcst_whitespace)
        else:
            whitespace = None

        libcst_comment: Optional[LibcstComment] = libcst_trailing_whitespace.comment
        comment: Optional[Comment]
        if libcst_comment is None:
            comment = None
        else:
            comment = CommentParser.parse_comment(libcst_comment)

        libcst_newline: LibcstNewline = libcst_trailing_whitespace.newline
        newline: Newline = NewlineParser.parse_newline(libcst_newline)

        trailing_whitespace = TrailingWhitespace(whitespace, comment, newline)

        return trailing_whitespace
