"""Deparser for Python subscript."""
from arborista.deparser import Deparser
from arborista.deparsers.python.index_deparser import IndexDeparser
from arborista.deparsers.python.slice_deparser import SliceDeparser
from arborista.nodes.python.index import Index
from arborista.nodes.python.slice import Slice
from arborista.nodes.python.subscript import Subscript


class SubscriptDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for Python subscript."""
    @staticmethod
    def deparse_subscript(subscript: Subscript) -> str:
        """Deparse Python subscript."""
        string: str

        if isinstance(subscript, Index):
            index: Index = subscript
            string = IndexDeparser.deparse_index(index)
        elif isinstance(subscript, Slice):
            slice_: Slice = subscript
            string = SliceDeparser.deparse_slice(slice_)
        else:
            raise NotImplementedError  # pragma: no cover

        return string
