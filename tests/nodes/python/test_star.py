"""Test arborista.nodes.python.star."""
from typing import Any

import pytest

from arborista.nodes.python.star import Star


# yapf: disable
@pytest.mark.parametrize('star, other, expected_equality', [
    (Star(), 'foo', False),
    (Star(), Star(), True),
])
# yapf: enable
def test_eq(star: Star, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.star.Star.__eq__."""
    equality: bool = star == other

    assert equality == expected_equality
