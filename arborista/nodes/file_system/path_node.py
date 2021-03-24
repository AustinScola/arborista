"""A file system path."""
from pathlib import Path
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.standard_equality import standard_equality

from arborista.node import Node


class PathNode(Node):
    """A file system path."""
    def __init__(self, path: Path, parent: Optional[Node] = None):
        super().__init__(parent)

        self.path: Path = path

    @standard_equality
    def __eq__(self, other: Any) -> bool:
        pass  # pragma: no cover
