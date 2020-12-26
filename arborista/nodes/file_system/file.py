"""A file system file."""
import os
from pathlib import Path
from typing import Any, Optional

from arborista.node import Node, NodeIterator


class File(Node):
    """A file system file."""
    def __init__(self, path: Path, contents: Node, parent: Optional[Node] = None):
        super().__init__(parent)

        self.path: Path = path
        self.contents: Node = contents

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, File):
            return False

        if os.path.normpath(self.path) != os.path.normpath(other.path):
            return False

        if self.contents != other.contents:
            return False

        return True

    def iterate_children(self) -> NodeIterator:
        yield self.contents

    @property
    def stem(self) -> str:
        """Return the stem of the file path."""
        return self.path.stem
