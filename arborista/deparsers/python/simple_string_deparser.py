"""Deparser for a Python simple string."""
from arborista.deparser import Deparser
from arborista.nodes.python.simple_string import SimpleString


class SimpleStringDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python simple string."""
    @staticmethod
    def deparse_simple_string(simple_string: SimpleString) -> str:
        """Deparse a Python simple string."""
        string: str = simple_string.value
        return string
