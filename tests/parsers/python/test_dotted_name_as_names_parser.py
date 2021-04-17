"""Test arborista.parsers.python.dotted_name_as_names_parser."""
from typing import List

import libcst
import pytest

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.dotted_name_as_names_parser import (DottedNameAsNamesParser,
                                                                  LibcstDottedNameAsNames)


def test_libcst_dotted_name_as_names() -> None:
    """Test arborista.parsers.python.dotted_name_as_names_parser.LibcstDottedNameAsNames."""
    assert isinstance(LibcstDottedNameAsNames, type(List))
    assert LibcstDottedNameAsNames.__args__ == (libcst.ImportAlias, )  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.parsers.python.dotted_name_as_names_parser.DottedNameAsNamesParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(DottedNameAsNamesParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_dotted_name_as_names, expected_dotted_name_as_names', [
    ([libcst.ImportAlias(libcst.Name('foo'))], DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), [])),
    ([libcst.ImportAlias(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')))], DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), [Name('bar')]), None), [])),
    ([libcst.ImportAlias(libcst.Name('foo')), libcst.ImportAlias(libcst.Name('bar')), libcst.ImportAlias(libcst.Name('baz'))], DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), [DottedNameAsName(DottedName(Name('bar'), []), None), DottedNameAsName(DottedName(Name('baz'), []), None)])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_dotted_name_as_names(libcst_dotted_name_as_names: LibcstDottedNameAsNames,
                                    expected_dotted_name_as_names: DottedNameAsNames) -> None:
    """Test arborista.parsers.python.dotted_name_as_names_parser.DottedNameAsNamesParser.parse_dotted_name_as_names."""  # pylint: disable=line-too-long, useless-suppression
    dotted_name_as_names: DottedNameAsNames = DottedNameAsNamesParser.parse_dotted_name_as_names(
        libcst_dotted_name_as_names)

    assert dotted_name_as_names == expected_dotted_name_as_names
