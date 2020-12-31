"""Deparser for a Python imaginary."""
from typing import Union

from arborista.deparser import Deparser
from arborista.nodes.python.imaginary import Imaginary


class ImaginaryDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python imaginary."""
    @staticmethod
    def deparse_imaginary(imaginary: Imaginary) -> str:
        """Deparse a Python imaginary."""
        value: Union[int, float] = imaginary.value
        string: str = f'{value}j'
        return string
