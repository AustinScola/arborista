"""Test arborista.nodes.python.break_statement."""
from typing import Any

import pytest

from arborista.nodes.python.break_statement import BreakStatement
from arborista.nodes.python.flow_statement import FlowStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.break_statement.BreakStatement inheritance."""
    assert issubclass(BreakStatement, FlowStatement)


# yapf: disable
@pytest.mark.parametrize('break_statement, other, expected_equality', [
    (BreakStatement(), 'foo', False),
    (BreakStatement(), BreakStatement(), True),
])
# yapf: enable
def test_eq(break_statement: BreakStatement, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.break_statement.BreakStatement.__eq__."""
    equality: bool = break_statement == other
    assert equality == expected_equality
