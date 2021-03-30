"""Deparser for a Python joined string."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.simple_string_deparser import SimpleStringDeparser
from arborista.nodes.python.joined_string import JoinedString
from arborista.nodes.python.simple_string import SimpleString


class JoinedStringDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python joined string."""
    @staticmethod
    def deparse_joined_string(joined_string: JoinedString) -> str:
        """Deparse a Python joined string."""
        string: str

        strings: List[str] = []
        for string_node in joined_string.strings:
            if isinstance(string_node, SimpleString):
                simple_string: SimpleString = string_node
                deparsed_string: str = SimpleStringDeparser.deparse_simple_string(simple_string)
                strings.append(deparsed_string)
            else:
                raise NotImplementedError  # pragma: no cover

        string = ' '.join(strings)
        return string
