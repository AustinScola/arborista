"""Test arborista.nodes.python.name."""
from typing import Any, Dict, Iterable, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.name import Name, Names
from arborista.nodes.python.parameter import Parameter


def test_inheritance() -> None:
    """Test arborista.nodes.python.name.Name inheritance."""
    assert issubclass(Name, Atom)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('f', None, False),
    ('f', None, True),
    ('f', Parameter(Name('f')), True),
])
# yapf: enable
def test_init(value: str, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.name.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    name: Name = Name(value, **keyword_arguments)

    assert name.value == value
    assert name.parent is parent


def test_names() -> None:
    """Test arborista.nodes.python.name.Names."""
    assert issubclass(Names, Iterable)
    assert Names.__args__ == (Name, )  # type: ignore[attr-defined]
