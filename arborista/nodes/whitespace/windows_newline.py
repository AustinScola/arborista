"""Windows newline characters."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.whitespace.newline import Newline


class WindowsNewline(Newline):
    """Windows newline characters."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True

    def __str__(self) -> str:
        return '\r\n'
