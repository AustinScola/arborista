"""Deparser for Python subscripts."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.subscript_deparser import SubscriptDeparser
from arborista.nodes.python.subscript import Subscript
from arborista.nodes.python.subscripts import Subscripts


class SubscriptsDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for Python subscripts."""
    @staticmethod
    def deparse_subscripts(subscripts: Subscripts) -> str:
        """Deparse Python subscripts."""
        string: str

        first: Subscript = subscripts.first
        first_string = SubscriptDeparser.deparse_subscript(first)

        rest: List[Subscript] = subscripts.rest
        rest_strings = (SubscriptDeparser.deparse_subscript(subscript) for subscript in rest)

        string = first_string + ''.join(', ' + subscript_string
                                        for subscript_string in rest_strings)

        return string
