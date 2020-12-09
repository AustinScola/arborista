"""Deparser for a Python name."""
from arborista.deparser import Deparser
from arborista.nodes.python.name import Name


class NameDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python name."""
    @staticmethod
    def deparse_name(name: Name) -> str:
        """Deparse a Python name."""
        return name.value
