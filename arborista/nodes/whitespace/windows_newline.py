"""Windows newline characters."""
from typing import Any

from arborista.nodes.whitespace.newline import Newline


class WindowsNewline(Newline):
    """Windows newline characters."""
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, WindowsNewline)

    def __str__(self) -> str:
        return '\r\n'
