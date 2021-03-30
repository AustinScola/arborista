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

    def run(self, tree: Tree) -> Tree:  # pylint: disable=too-many-branches
        """Return a transformed tree."""
        tree.set_parents()

        while True:  # pylint: disable=too-many-nested-blocks
            tree_changed: bool = False

            node_queue: Deque = deque([tree.root])
            removed_node_ids: Set[int] = set()

            while True:
                try:
                    node = node_queue.pop()
                except IndexError:
                    break

                if id(node) in removed_node_ids:
                    continue  # pragma: no cover

                while True:
                    node_is_root: bool = node is tree.root

                    node_type: NodeType = type(node)
                    transformations: TransformationSet = self._get_transformations_for_node_type(
                        node_type)

                    change_made: bool = False
                    node_type_changed: bool = False
                    while not node_type_changed:

                        transformation_result: TransformationResult
                        change_made = False
                        for transformation in transformations:
                            transformation_result = transformation.maybe_transform(node)
                            node = transformation_result.transformed_node
                            change_made = change_made or transformation_result.changed

                            if transformation_result.transformed_node is None:
                                if node_is_root:
                                    tree.root = None

                            transformed_node_type = type(transformation_result.transformed_node)
                            if transformed_node_type != node_type:
                                node_type_changed = True
                                if node_is_root:
                                    tree.root = node
                                break

                        if not change_made:
                            break

                    tree_changed = tree_changed or change_made
                    if not change_made:
                        break

                if node is not None:
                    children: NodeIterator = node.iterate_children()
                    node_queue.extend(children)

            if not tree_changed:
                break

        return tree

    def _get_transformations_for_node_type(self, node_type: NodeType) -> TransformationSet:
        """Return the set of transformations which can be run on the given node type."""
        transformations: TransformationSet = self._node_type_to_transformations[node_type]

        parent_node_types: Tuple[type, ...] = node_type.__bases__
        for parent_node_type in parent_node_types:
            transformation_for_parent_type: TransformationSet = self._node_type_to_transformations[  # pylint: disable=line-too-long, useless-suppression
                parent_node_type]
            transformations.update(transformation_for_parent_type)

        return transformations
