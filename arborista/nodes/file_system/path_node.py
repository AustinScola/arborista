"""A file system path."""
from pathlib import Path
from typing import Any, Optional

from arborista.node import Node


class PathNode(Node):
    """A file system path."""
    def __init__(self, path: Path, parent: Optional[Node] = None):
        super().__init__(parent)

        self.path: Path = path

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PathNode):
            return False

        return self.path == other.path
