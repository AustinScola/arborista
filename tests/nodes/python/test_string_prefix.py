"""Test arborista.nodes.python.string_prefix."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.string_prefix import StringPrefix, StringPrefixValue


def test_string_prefix_value() -> None:
    """Test arborista.nodes.python.string_prefix.StringPrefixValue."""
    assert isinstance(StringPrefixValue, type(Literal))
    assert StringPrefixValue.__values__ == (  # type: ignore[attr-defined]
        'f', 'r', 'u', 'F', 'R', 'U', 'fr', 'Fr', 'fR', 'FR', 'rf', 'Rf', 'rF', 'RF')


def test_inheritance() -> None:
    """Test arborista.nodes.python.string_prefix.StringPrefix inheritance."""
    assert issubclass(StringPrefix, PythonNode)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('f', None, False),
    ('f', None, True),
    ('f', MagicMock(), True),
])
# yapf: enable
def test_init(value: StringPrefixValue, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.string_prefix.StringPrefix.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    string_prefix: StringPrefix = StringPrefix(value, **keyword_arguments)

    assert string_prefix.value == value
    assert string_prefix.parent is parent
