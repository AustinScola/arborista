"""Test arborista.deparsers.python.dotted_name_as_name_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.dotted_name_as_name_deparser import DottedNameAsNameDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.dotted_name_as_name_deparser.DottedNameAsNameDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(DottedNameAsNameDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('dotted_name_as_name, expected_string', [
    (DottedNameAsName(DottedName(Name('foo'), []), None), 'foo'),
    (DottedNameAsName(DottedName(Name('foo'), []), Name('bar')), 'foo as bar'),
])
# yapf: enable
def test_deparse_dotted_name_as_name(dotted_name_as_name: DottedNameAsName,
                                     expected_string: str) -> None:
    """Test arborista.deparsers.python.dotted_name_as_name_deparser.DottedNameAsNameDeparser.deparse_dotted_name_as_name."""  # pylint: disable=line-too-long, useless-suppression
    string: str = DottedNameAsNameDeparser.deparse_dotted_name_as_name(dotted_name_as_name)

    assert string == expected_string
