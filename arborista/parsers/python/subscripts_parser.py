"""A parser for Python subscripts."""
from typing import List, Sequence

import libcst

from arborista.nodes.python.subscript import Subscript
from arborista.nodes.python.subscripts import Subscripts
from arborista.parser import Parser
from arborista.parsers.python.subscript_parser import LibcstSubscript, SubscriptParser

LibcstSubscripts = Sequence[libcst.SubscriptElement]


class SubscriptsParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for Python subscripts."""
    @staticmethod
    def parse_subscripts(libcst_subscripts: LibcstSubscripts) -> Subscripts:
        """Parser Python subscripts."""
        libcst_first: LibcstSubscript = libcst_subscripts[0]
        first: Subscript = SubscriptParser.parse_subscript(libcst_first)

        libcst_rest: List[LibcstSubscript] = list(libcst_subscripts[1:])
        rest: List[Subscript] = [
            SubscriptParser.parse_subscript(libcst_subscript) for libcst_subscript in libcst_rest
        ]

        subscripts: Subscripts = Subscripts(first, rest)
        return subscripts
