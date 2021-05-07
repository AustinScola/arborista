"""Test arborista.nodes.python.newline."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.newline import Newline
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.newline.Newline inheritance."""
    assert issubclass(Newline, PythonNode)


_PARENT = MagicMock()


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_value, expected_parent', [
    ([], {}, '\n', None),
    ([], {'parent': None}, '\n', None),
    ([], {'parent': _PARENT}, '\n', _PARENT),
    (['\n'], {}, '\n', None),
    (['\r\n'], {}, '\r\n', None),
])
# yapf: enable
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any], expected_value: str,
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.newline.Newline.__init__."""
    newline: Newline = Newline(*arguments, **keyword_arguments)

    assert newline.value == expected_value
    assert newline.parent is expected_parent
