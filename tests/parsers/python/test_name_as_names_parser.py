"""Test arborista.parsers.python.name_as_names_parser."""
from typing import Sequence

import libcst
import pytest

from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.parser import Parser
from arborista.parsers.python.name_as_names_parser import LibcstNameAsNames, NameAsNamesParser


def test_libcst_name_as_names() -> None:
    """Test arborista.parsers.python.name_as_names_parser.LibcstNameAsNames."""
    assert isinstance(LibcstNameAsNames, type(Sequence))
    assert LibcstNameAsNames.__args__ == (libcst.ImportAlias, )  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.parsers.python.name_as_names_parser.NameAsNamesParser inheritance."""
    assert issubclass(NameAsNamesParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_name_as_names, expected_name_as_names', [
    ([libcst.ImportAlias(libcst.Name('foo'), libcst.AsName(libcst.Name('bar')))], NameAsNames(NameAsName(Name('foo'), Name('bar')), [])),
    ([libcst.ImportAlias(libcst.Name('foo')), libcst.ImportAlias(libcst.Name('bar')), libcst.ImportAlias(libcst.Name('baz'))], NameAsNames(NameAsName(Name('foo'), None), [NameAsName(Name('bar'), None), NameAsName(Name('baz'), None)])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_name_as_names(libcst_name_as_names: LibcstNameAsNames,
                             expected_name_as_names: NameAsNames) -> None:
    """Test arborista.parsers.python.name_as_names_parser.NameAsNamesParser.parse_name_as_names."""
    name_as_names: NameAsNames = NameAsNamesParser.parse_name_as_names(libcst_name_as_names)

    assert name_as_names == expected_name_as_names
