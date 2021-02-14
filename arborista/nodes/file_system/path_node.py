"""A file system path."""
from pathlib import Path
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node


class PathNode(Node):
    """A file system path."""
    def __init__(self, path: Path, parent: Optional[Node] = None):
        super().__init__(parent)

        self.path: Path = path

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.path == other.path
        return equality
