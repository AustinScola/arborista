"""A Linux newline character."""
from typing import Any

from arborista.nodes.whitespace.newline import Newline


class LinuxNewline(Newline):
    """A Linux newline character."""
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, LinuxNewline)

    def __str__(self) -> str:
        return '\n'
