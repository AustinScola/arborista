"""Test arborista.parsers.python.atom_parser."""
from typing import Union

import libcst
import pytest

from arborista.nodes.python.atom import Atom
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.name import Name
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String
from arborista.parser import Parser
from arborista.parsers.python.atom_parser import AtomParser, LibcstAtom
from arborista.parsers.python.name_parser import LibcstName
from arborista.parsers.python.number_parser import LibcstNumber


def test_libcst_atom() -> None:
    """Test arborista.parsers.python.atom_parser.LibcstAtom"""
    assert isinstance(LibcstAtom, type(Union))
    assert LibcstAtom.__args__ == (  # type: ignore[attr-defined]
        LibcstName, LibcstNumber, libcst.SimpleString, libcst.FormattedString)


def test_inheritance() -> None:
    """Test arborista.parsers.python.atom_parser.AtomParser inheritance."""
    assert issubclass(AtomParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_atom, expected_atom', [
    (libcst.Integer('1'), Integer(1)),
    (libcst.SimpleString("'foo'"), String(None, SingleQuotedShortString('foo'))),
    (libcst.Name('foo'), Name('foo')),
])
# yapf: enable
def test_parse_atom(libcst_atom: LibcstAtom, expected_atom: Atom) -> None:
    """Test arborista.parsers.python.atom_parser.AtomParser.parse_atom."""
    atom: Atom = AtomParser.parse_atom(libcst_atom)

    assert atom == expected_atom
