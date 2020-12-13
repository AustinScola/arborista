"""A transformation of a node."""
from abc import ABC, abstractmethod
from typing import Iterable, Optional

from arborista.node import Node


class Transformation(ABC):  # pylint: disable=too-few-public-methods
    """A transformation of a node."""
    @staticmethod
    @abstractmethod
    def maybe_transform(node: Node) -> Optional[Node]:
        """Returns a transformed node or returns None to trim this node from the tree."""
        raise NotImplementedError


Transformations = Iterable[Transformation]
