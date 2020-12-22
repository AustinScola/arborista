"""This module transforms abstract syntax trees."""
import logging
from collections import defaultdict, deque
from typing import Deque, Dict, Set, Tuple

from arborista.node import NodeIterator, NodeType
from arborista.transformation import Transformations, TransformationSet
from arborista.transformation_result import TransformationResult
from arborista.tree import Tree

LOGGER = logging.getLogger(__name__)


class Transformer():  # pylint: disable=too-few-public-methods
    """Transform a tree using a set of transformations."""
    def __init__(self, transformations: Transformations) -> None:
        self.transformations: TransformationSet = set(transformations)

        self._node_type_to_transformations: Dict[NodeType, TransformationSet] = defaultdict(set)
        for transformation in transformations:
            for node_type in transformation.NODE_TYPES:
                self._node_type_to_transformations[node_type].add(transformation)

    def run(self, tree: Tree) -> Tree:
        """Return a transformed tree."""
        tree.set_parents()

        node_queue: Deque = deque([tree.root])
        removed_node_ids: Set[int] = set()
        while True:
            try:
                node = node_queue.pop()
            except IndexError:
                break

            if id(node) in removed_node_ids:
                continue

            node_type: NodeType = type(node)
            transformations: TransformationSet = self._get_transformations_for_node_type(node_type)

            transformation_result: TransformationResult
            for transformation in transformations:
                transformation_result = transformation.maybe_transform(node)
                node = transformation_result.transformed_node

                if transformation_result.transformed_node is None:
                    raise NotImplementedError

                transformed_node_type = type(transformation_result.transformed_node)
                if transformed_node_type != node_type:
                    raise NotImplementedError

            if node is not None:
                children: NodeIterator = node.iterate_children()
                node_queue.extend(children)

        return tree

    def _get_transformations_for_node_type(self, node_type: NodeType) -> TransformationSet:
        """Return the set of transformations which can be run on the given node type."""
        transformations: TransformationSet = self._node_type_to_transformations[node_type]

        parent_node_types: Tuple[type, ...] = node_type.__bases__
        for parent_node_type in parent_node_types:
            try:
                transformation_for_parent_type: TransformationSet = self._node_type_to_transformations[  # pylint: disable=line-too-long, useless-suppression
                    parent_node_type]
            except KeyError:
                continue
            transformations.update(transformation_for_parent_type)

        return transformations
