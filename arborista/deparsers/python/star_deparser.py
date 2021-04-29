"""Deparser for a Python star."""
from arborista.deparser import Deparser
from arborista.nodes.python.star import Star


class StarDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python star."""
    @staticmethod
    def deparse_star(star: Star) -> str:  # pylint: disable=unused-argument
        """Deparse a Python star."""
        return '*'
