"""A transformation of a node."""
from abc import ABC, abstractmethod
from typing import Iterable, List, Optional, Set

from arborista.node import Node, NodeTypeSet


class Transformation(ABC):  # pylint: disable=too-few-public-methods
    """A transformation of a node."""
    NODE_TYPES: NodeTypeSet = set()

    @classmethod
    @abstractmethod
    def maybe_transform(cls, node: Node) -> Optional[Node]:
        """Returns a transformed node or returns None to trim this node from the tree."""
        raise NotImplementedError


Transformations = Iterable[Transformation]
TransformationList = List[Transformation]
TransformationSet = Set[Transformation]
