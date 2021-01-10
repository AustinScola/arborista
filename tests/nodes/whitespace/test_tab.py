"""Test arborista.nodes.whitespace.tab."""
from typing import Any

import pytest

from arborista.nodes.whitespace.tab import Tab
from arborista.nodes.whitespace.whitespace import Whitespace


def test_inheritance() -> None:
    """Test arborista.nodes.whitespace.tab.Tab inheritance."""
    assert issubclass(Tab, Whitespace)


# yapf: disable
@pytest.mark.parametrize('tab, other, expected_equality', [
    (Tab(), 'foo', False),
    (Tab(), Tab(), True),
])
# yapf: enable
def test_eq(tab: Tab, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.whitespace.tab.Tab.__eq__."""
    equality: bool = tab == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('tab, expected_string', [
    (Tab(), '\t'),
])
# yapf: enable
def test_str(tab: Tab, expected_string: str) -> None:
    """Test arborista.nodes.whitespace.tab.Tab.__str__."""
    string: str = str(tab)

    assert string == expected_string
