"""Parser for a Python atom."""
from typing import Union

import libcst

from arborista.nodes.python.atom import Atom
from arborista.nodes.python.number import Number
from arborista.nodes.python.string import String
from arborista.parser import Parser
from arborista.parsers.python.number_parser import LibcstNumber, NumberParser
from arborista.parsers.python.string_parser import LibcstString, StringParser

LibcstAtom = Union[LibcstNumber, libcst.SimpleString, libcst.FormattedString]


class AtomParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python atom."""
    @staticmethod
    def parse_atom(libcst_atom: LibcstAtom) -> Atom:
        """Parse a Python atom."""
        atom: Atom

        if isinstance(libcst_atom, LibcstNumber):
            libcst_number: LibcstNumber = libcst_atom
            number: Number = NumberParser.parse_number(libcst_number)
            atom = number
        elif isinstance(libcst_atom, (libcst.SimpleString, libcst.FormattedString)):
            libcst_string: LibcstString = libcst_atom
            string: String = StringParser.parse_string(libcst_string)
            atom = string
        else:
            raise NotImplementedError  # pragma: no cover

        return atom
