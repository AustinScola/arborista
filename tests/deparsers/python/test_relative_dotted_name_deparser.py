"""Test arborista.deparsers.python.relative_dotted_name_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.relative_dotted_name_deparser import RelativeDottedNameDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.nodes.python.relative_dotted_name import RelativeDottedName


def test_inheritance() -> None:
    """Test arborista.deparsers.python.relative_dotted_name_deparser.RelativeDottedNameDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(RelativeDottedNameDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('relative_dotted_name, expected_string', [
    (RelativeDottedName(1, None), '.'),
    (RelativeDottedName(1, DottedName(Name('foo'), [])), '.foo'),
    (RelativeDottedName(2, DottedName(Name('foo'), [])), '..foo'),
    (RelativeDottedName(3, DottedName(Name('foo'), [])), '...foo'),
])
# yapf: enable
def test_deparse_relative_dotted_name(relative_dotted_name: RelativeDottedName,
                                      expected_string: str) -> None:
    """Test arborista.deparsers.python.relative_dotted_name_deparser.RelativeDottedNameDeparser.deparse_relative_dotted_name."""  # pylint: disable=line-too-long, useless-suppression
    string: str = RelativeDottedNameDeparser.deparse_relative_dotted_name(relative_dotted_name)

    assert string == expected_string
