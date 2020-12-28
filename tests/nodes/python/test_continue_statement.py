"""Test arborista.nodes.python.continue_statement."""
from typing import Any

import pytest

from arborista.nodes.python.continue_statement import ContinueStatement
from arborista.nodes.python.flow_statement import FlowStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.continue_statement.ContinueStatement inheritance."""
    assert issubclass(ContinueStatement, FlowStatement)


# yapf: disable
@pytest.mark.parametrize('continue_statement, other, expected_equality', [
    (ContinueStatement(), 'foo', False),
    (ContinueStatement(), ContinueStatement(), True),
])
# yapf: enable
def test_eq(continue_statement: ContinueStatement, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.continue_statement.ContinueStatement.__eq__."""
    equality: bool = continue_statement == other

    assert equality == expected_equality
