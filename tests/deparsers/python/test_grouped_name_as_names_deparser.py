"""Test arborista.deparsers.python.grouped_name_as_names_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.grouped_name_as_names_deparser import GroupedNameAsNamesDeparser
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames


def test_inheritance() -> None:
    """Test arborista.deparsers.python.grouped_name_as_names_deparser.GroupedNameAsNamesDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(GroupedNameAsNamesDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('grouped_name_as_names, expected_string', [
    (GroupedNameAsNames(NameAsNames(NameAsName(Name('foo'), None), [])), '(foo)'),
])
# yapf: enable
def test_deparse_grouped_name_as_names(grouped_name_as_names: GroupedNameAsNames,
                                       expected_string: str) -> None:
    """Test arborista.deparsers.python.grouped_name_as_names_deparser.GroupedNameAsNamesDeparser.deparse_grouped_name_as_names."""  # pylint: disable=line-too-long, useless-suppression
    string: str = GroupedNameAsNamesDeparser.deparse_grouped_name_as_names(grouped_name_as_names)

    assert string == expected_string
