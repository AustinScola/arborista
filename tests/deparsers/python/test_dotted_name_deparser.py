"""Test arborista.deparsers.python.dotted_name_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.dotted_name_deparser import DottedNameDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.dotted_name_deparser.DottedNameDeparser inheritance."""
    assert issubclass(DottedNameDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('dotted_name, expected_string', [
    (DottedName(Name('foo'), []), 'foo'),
    (DottedName(Name('foo'), [Name('bar')]), 'foo.bar'),
    (DottedName(Name('foo'), [Name('bar'), Name('baz')]), 'foo.bar.baz'),
])
# yapf: enable
def test_deparse_dotted_name(dotted_name: DottedName, expected_string: str) -> None:
    """Test arborista.deparsers.python.dotted_name_deparser.DottedNameDeparser.deparse_dotted_name."""  # pylint: disable=line-too-long, useless-suppression
    string: str = DottedNameDeparser.deparse_dotted_name(dotted_name)

    assert string == expected_string
