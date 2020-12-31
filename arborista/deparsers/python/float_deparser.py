"""Deparser for a Python float."""
from arborista.deparser import Deparser
from arborista.nodes.python.float import Float


class FloatDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python float."""
    @staticmethod
    def deparse_float(float_: Float) -> str:
        """Deparse a Python float."""
        value: float = float_.value
        string: str = str(value)
        return string
