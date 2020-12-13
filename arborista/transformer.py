"""This module transforms abstract syntax trees."""
import logging

from arborista.transformation import Transformations, TransformationSet
from arborista.tree import Tree

LOGGER = logging.getLogger(__name__)


class Transformer():  # pylint: disable=too-few-public-methods
    """Transform a tree using a set of transformations."""
    def __init__(self, transformations: Transformations) -> None:
        self.transformations: TransformationSet = set(transformations)

    def run(self, tree: Tree) -> Tree:
        """Return a transformed tree."""
        raise NotImplementedError
