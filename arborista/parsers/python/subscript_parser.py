"""A parser for a Python subscript."""
import libcst

from arborista.nodes.python.index import Index
from arborista.nodes.python.slice import Slice
from arborista.nodes.python.subscript import Subscript
from arborista.parser import Parser
from arborista.parsers.python.index_parser import IndexParser, LibcstIndex
from arborista.parsers.python.slice_parser import LibcstSlice, SliceParser

LibcstSubscript = libcst.SubscriptElement


class SubscriptParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python subscript."""
    @staticmethod
    def parse_subscript(libcst_subscript: LibcstSubscript) -> Subscript:
        """Parse a Python subscript."""
        subscript: Subscript

        if isinstance(libcst_subscript.slice, LibcstIndex):
            libcst_index: LibcstIndex = libcst_subscript.slice
            index: Index = IndexParser.parse_index(libcst_index)
            subscript = index
        elif isinstance(libcst_subscript.slice, LibcstSlice):
            libcst_slice: LibcstSlice = libcst_subscript.slice
            slice_: Slice = SliceParser.parse_slice(libcst_slice)
            subscript = slice_
        else:
            raise NotImplementedError

        return subscript
