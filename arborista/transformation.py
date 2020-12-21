"""A transformation of a node."""
from abc import ABC, abstractmethod
from typing import Iterable, List, Set

from arborista.node import Node, NodeTypeSet
from arborista.transformation_result import TransformationResult


class Transformation(ABC):  # pylint: disable=too-few-public-methods
    """A transformation of a node."""
    NODE_TYPES: NodeTypeSet = set()

    @classmethod
    @abstractmethod
    def maybe_transform(cls, node: Node) -> TransformationResult:
        """Maybe transforms nodes and returns an iterator of nodes which were removed (if any)."""
        raise NotImplementedError


Transformations = Iterable[Transformation]
TransformationList = List[Transformation]
TransformationSet = Set[Transformation]
