"""Deparser for a Python joined string."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.string_deparser import StringDeparser
from arborista.nodes.python.joined_string import JoinedString


class JoinedStringDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python joined string."""
    @staticmethod
    def deparse_joined_string(joined_string: JoinedString) -> str:
        """Deparse a Python joined string."""
        string: str

        strings: List[str] = []
        for string_node in joined_string.strings:
            deparsed_string: str = StringDeparser.deparse_string(string_node)
            strings.append(deparsed_string)

        string = ' '.join(strings)
        return string
