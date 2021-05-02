"""Test arborista.deparsers.python.atom_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.atom_deparser import AtomDeparser
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.name import Name
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String


def test_inheritance() -> None:
    """Test arborista.deparsers.python.atom_deparser.AtomDeparser inheritance."""
    assert issubclass(AtomDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('atom, expected_string', [
    (String(None, SingleQuotedShortString('foo')), "'foo'"),
    (Name('foo'), 'foo'),
    (DottedName(Name('foo'), []), 'foo'),
    (Integer(1), '1'),
])
# yapf: enable
def test_deparse_atom(atom: Atom, expected_string: str) -> None:
    """Test arborista.deparsers.python.atom_deparser.AtomDeparser.deparse_atom."""
    string: str = AtomDeparser.deparse_atom(atom)

    assert string == expected_string
