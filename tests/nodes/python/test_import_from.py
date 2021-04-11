"""Test arborista.nodes.python.import_from."""
from typing import Any, Dict, Optional, Union
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.import_from import ImportFrom, Source, Target
from arborista.nodes.python.import_statement import ImportStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.relative_dotted_name import RelativeDottedName
from arborista.nodes.python.star import Star


def test_source() -> None:
    """Test arborista.nodes.python.import_from.ImportFrom.Source."""
    assert isinstance(Source, type(Union))
    assert Source.__args__ == (DottedName, RelativeDottedName)  # type: ignore[attr-defined]


def test_target() -> None:
    """Test arborista.nodes.python.import_from.ImportFrom.Target."""
    assert isinstance(Target, type(Union))
    assert Target.__args__ == (Star, GroupedNameAsNames, NameAsNames)  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.nodes.python.import_from.ImportFrom inheritance."""
    assert issubclass(ImportFrom, ImportStatement)


# yapf: disable
@pytest.mark.parametrize('source, target, parent, pass_parent', [
    (DottedName(Name('foo'), []), Star(), None, False),
    (DottedName(Name('foo'), []), Star(), None, True),
    (DottedName(Name('foo'), []), Star(), MagicMock(), True),
])
# yapf: enable
def test_init(source: Source, target: Target, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.import_from.ImportFrom.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    import_from: ImportFrom = ImportFrom(source, target, **keyword_arguments)

    assert import_from.source == source
    assert import_from.target == target
    assert import_from.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('import_from, other, expected_equality', [
    (ImportFrom(DottedName(Name('foo'), []), Star()), 'foo', False),
    (ImportFrom(DottedName(Name('foo'), []), Star()), ImportFrom(DottedName(Name('foo'), []), NameAsNames(NameAsName(Name('foo')), [])), False),
    (ImportFrom(DottedName(Name('foo'), []), Star()), ImportFrom(DottedName(Name('bar'), []), Star()), False),
    (ImportFrom(DottedName(Name('foo'), []), Star()), ImportFrom(DottedName(Name('foo'), []), Star()), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(import_from: ImportFrom, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.import_from.ImportFrom.__eq__."""
    equality: bool = import_from == other

    assert equality == expected_equality
