"""Test arborista.nodes.whitespace.windows_newline."""
from typing import Any

import pytest

from arborista.nodes.whitespace.newline import Newline
from arborista.nodes.whitespace.windows_newline import WindowsNewline


def test_inheritance() -> None:
    """Test arborista.nodes.whitespace.windows_newline.WindowsNewline inheritance."""
    assert issubclass(WindowsNewline, Newline)


# yapf: disable
@pytest.mark.parametrize('windows_newline, other, expected_equality', [
    (WindowsNewline(), 'foo', False),
    (WindowsNewline(), WindowsNewline(), True),
])
# yapf: enable
def test_eq(windows_newline: WindowsNewline, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.whitespace.windows_newline.WindowsNewline.__eq__."""
    equality: bool = windows_newline == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('windows_newline, expected_string', [
    (WindowsNewline(), '\r\n'),
])
# yapf: enable
def test_str(windows_newline: WindowsNewline, expected_string: str) -> None:
    """Test arborista.nodes.whitespace.windows_newline.WindowsNewline.__str__."""
    string: str = str(windows_newline)

    assert string == expected_string
