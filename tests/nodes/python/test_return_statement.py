"""Test arborista.nodes.python.return_statement."""
from typing import Any

import pytest

from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.return_statement import ReturnStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.return_statement.ReturnStatement inheritance."""
    assert issubclass(ReturnStatement, FlowStatement)


# yapf: disable
@pytest.mark.parametrize('return_statement, other, expected_equality', [
    (ReturnStatement(), 'foo', False),
    (ReturnStatement(), ReturnStatement(), True),
])
# yapf: enable
def test_eq(return_statement: ReturnStatement, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.return_statement.ReturnStatement.__eq__."""
    equality: bool = return_statement == other
    assert equality == expected_equality
