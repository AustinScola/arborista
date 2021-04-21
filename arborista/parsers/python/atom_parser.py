"""Parser for a Python atom."""
from typing import Union

import libcst

from arborista.nodes.python.atom import Atom
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.nodes.python.number import Number
from arborista.nodes.python.string import String
from arborista.parser import Parser
from arborista.parsers.python.name_parser import LibcstName, NameParser
from arborista.parsers.python.number_parser import LibcstNumber, NumberParser
from arborista.parsers.python.string_parser import LibcstString, StringParser

LibcstAtom = Union[LibcstName, libcst.Attribute, LibcstNumber, libcst.SimpleString,
                   libcst.FormattedString]


class AtomParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python atom."""
    @staticmethod
    def parse_atom(libcst_atom: LibcstAtom) -> Atom:
        """Parse a Python atom."""
        from arborista.parsers.python.dotted_name_parser import (  # pylint: disable=import-outside-toplevel
            DottedNameParser, LibcstDottedName)

        atom: Atom

        if isinstance(libcst_atom, LibcstName):
            libcst_name: LibcstName = libcst_atom
            name: Name = NameParser.parse_name(libcst_name)
            atom = name
        elif isinstance(libcst_atom, LibcstDottedName):
            libcst_dotted_name: LibcstDottedName = libcst_atom
            dotted_name: DottedName = DottedNameParser.parse_dotted_name(libcst_dotted_name)
            atom = dotted_name
        elif isinstance(libcst_atom, LibcstNumber):
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
