"""A file system file."""
import os
from pathlib import Path
from typing import Any

from arborista.node import Node


class File(Node):
    """A file system file."""
    def __init__(self, path: Path, contents: str):
        self.path: Path = path
        self.contents: str = contents

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, File):
            return False

        if os.path.normpath(self.path) != os.path.normpath(other.path):
            return False

        if self.contents != other.contents:
            return False

        return True
