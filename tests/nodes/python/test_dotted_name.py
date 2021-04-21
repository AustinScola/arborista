"""Test arborista.nodes.python.dotted_name."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name, Names


def test_inheritance() -> None:
    """Test arborista.nodes.python.dotted_name.DottedName inheritance."""
    assert issubclass(DottedName, Atom)


# yapf: disable
@pytest.mark.parametrize('first_name, rest_of_names, parent, pass_parent', [
    (Name('foo'), [], None, False),
    (Name('foo'), [], None, True),
    (Name('foo'), [], MagicMock(), True),
    (Name('foo'), [Name('bar'), Name('bar')], None, False),
    (Name('foo'), [Name('bar'), Name('bar')], None, True),
    (Name('foo'), [Name('bar'), Name('bar')], MagicMock(), True),
])
# yapf: enable
def test_init(first_name: Name, rest_of_names: Names, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.dotted_name.DottedName.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    dotted_name: DottedName = DottedName(first_name, rest_of_names, **keyword_arguments)

    assert dotted_name.first_name == first_name
    assert dotted_name.rest_of_names == rest_of_names
    assert dotted_name.parent is parent
