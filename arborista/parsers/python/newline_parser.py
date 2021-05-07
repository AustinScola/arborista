"""Parser for newline."""
from typing import Optional

import libcst

from arborista.nodes.python.newline import Newline
from arborista.parser import Parser

LibcstNewline = libcst.Newline


class NewlineParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for newline."""
    @staticmethod
    def parse_newline(libcst_newline: LibcstNewline) -> Newline:
        """Parse newline."""
        libcst_value: Optional[str] = libcst_newline.value
        value: str = '\n' if libcst_value is None else libcst_value

        newline: Newline = Newline(value)

        return newline
