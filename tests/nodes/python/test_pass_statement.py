"""Test arborista.nodes.python.pass_statement."""
from typing import Any

import pytest

from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.small_statement import SmallStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.pass_statement.PassStatement inheritance."""
    assert issubclass(PassStatement, SmallStatement)


# yapf: disable
@pytest.mark.parametrize('pass_statement, other, expected_equality', [
    (PassStatement(), 'foo', False),
    (PassStatement(), PassStatement(), True),
])
# yapf: enable
def test_eq(pass_statement: PassStatement, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.pass_statement.PassStatement.__eq__."""
    equality: bool = pass_statement == other
    assert equality == expected_equality
