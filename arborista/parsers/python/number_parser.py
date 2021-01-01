"""Parser for a Python number."""
import libcst

from arborista.nodes.python.float import Float
from arborista.nodes.python.imaginary import Imaginary
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.number import Number
from arborista.parser import Parser
from arborista.parsers.python.float_parser import FloatParser, LibcstFloat
from arborista.parsers.python.imaginary_parser import ImaginaryParser, LibcstImaginary
from arborista.parsers.python.integer_parser import IntegerParser, LibcstInteger

LibcstNumber = libcst.BaseNumber


class NumberParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python number."""
    @staticmethod
    def parse_number(libcst_number: LibcstNumber) -> Number:
        """Parse a Python number."""
        number: Number
        if isinstance(libcst_number, LibcstInteger):
            libcst_integer: LibcstInteger = libcst_number
            integer: Integer = IntegerParser.parse_integer(libcst_integer)
            number = integer
        elif isinstance(libcst_number, LibcstFloat):
            libcst_float: LibcstFloat = libcst_number
            float_: Float = FloatParser.parse_float(libcst_float)
            number = float_
        elif isinstance(libcst_number, LibcstImaginary):
            libcst_imaginary: LibcstImaginary = libcst_number
            imaginary: Imaginary = ImaginaryParser.parse_imaginary(libcst_imaginary)
            number = imaginary
        return number
