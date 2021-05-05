"""Test arborista.nodes.python.return_statement."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.return_statement import ReturnStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.return_statement.ReturnStatement inheritance."""
    assert issubclass(ReturnStatement, FlowStatement)


_parent = MagicMock()


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_value, expected_parent', [
    ([], {}, None, None),
    ([Name('foo')], {}, Name('foo'), None),
    ([], {'parent': None}, None, None),
    ([], {'parent': _parent}, None, _parent),
])
# yapf: enable
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
              expected_value: Optional[Expression], expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.return_statement.ReturnStatement.__init__."""
    return_statement: ReturnStatement = ReturnStatement(*arguments, **keyword_arguments)

    assert return_statement.value == expected_value
    assert return_statement.parent is expected_parent
