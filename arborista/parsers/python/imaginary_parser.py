"""Parser for a Python imaginary."""
from typing import Union

import libcst

from arborista.nodes.python.imaginary import Imaginary
from arborista.parser import Parser

LibcstImaginary = libcst.Imaginary


class ImaginaryParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python imaginary."""
    @staticmethod
    def parse_imaginary(libcst_imaginary: LibcstImaginary) -> Imaginary:
        """Parser a Python imaginary."""
        libcst_value: str = libcst_imaginary.value
        value: Union[int, float] = complex(libcst_value).imag
        imaginary: Imaginary = Imaginary(value)
        return imaginary
