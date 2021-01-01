"""Deparser for a Python number."""
from arborista.deparser import Deparser
from arborista.deparsers.python.float_deparser import FloatDeparser
from arborista.deparsers.python.imaginary_deparser import ImaginaryDeparser
from arborista.deparsers.python.integer_deparser import IntegerDeparser
from arborista.nodes.python.float import Float
from arborista.nodes.python.imaginary import Imaginary
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.number import Number


class NumberDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python number."""
    @staticmethod
    def deparse_number(number: Number) -> str:
        """Deparse a Python number."""
        string: str
        if isinstance(number, Integer):
            integer: Integer = number
            integer_string = IntegerDeparser.deparse_integer(integer)
            string = integer_string
        elif isinstance(number, Float):
            float_: Float = number
            float_string = FloatDeparser.deparse_float(float_)
            string = float_string
        elif isinstance(number, Imaginary):
            imaginary: Imaginary = number
            imaginary_string = ImaginaryDeparser.deparse_imaginary(imaginary)
            string = imaginary_string
        return string
