"""Test arborista.nodes.whitespace.linux_newline."""
from typing import Any

import pytest

from arborista.nodes.whitespace.linux_newline import LinuxNewline
from arborista.nodes.whitespace.newline import Newline


def test_inheritance() -> None:
    """Test arborista.nodes.whitespace.linux_newline.LinuxNewline inheritance."""
    assert issubclass(LinuxNewline, Newline)


# yapf: disable
@pytest.mark.parametrize('linux_newline, other, expected_equality', [
    (LinuxNewline(), 'foo', False),
    (LinuxNewline(), LinuxNewline(), True),
])
# yapf: enable
def test_eq(linux_newline: LinuxNewline, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.whitespace.linux_newline.LinuxNewline.__eq__."""
    equality: bool = linux_newline == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('linux_newline, expected_string', [
    (LinuxNewline(), '\n'),
])
# yapf: enable
def test_str(linux_newline: LinuxNewline, expected_string: str) -> None:
    """Test arborista.nodes.whitespace.linux_newline.LinuxNewline.__str__."""
    string: str = str(linux_newline)

    assert string == expected_string
