"""Parser for a Python float."""
import libcst

from arborista.nodes.python.float import Float
from arborista.parser import Parser

LibcstFloat = libcst.Float


class FloatParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python float."""
    @staticmethod
    def parse_float(libcst_float: LibcstFloat) -> Float:
        """Parser a Python float."""
        libcst_value: str = libcst_float.value
        value: float = float(libcst_value)
        float_: Float = Float(value)
        return float_
