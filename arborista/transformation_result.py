"""The result of a transformation."""
from typing import Any, Optional, Set

from arborista.node import Node, NodeIterable, NodeList


class TransformationResult():  # pylint: disable=too-few-public-methods
    """The result of a transformation."""
    def __init__(self, transformed_node: Optional[Node], changed: bool,
                 removed_nodes: NodeIterable):
        self.transformed_node: Optional[Node] = transformed_node
        self.changed: bool = changed
        self.removed_nodes: NodeList = list(removed_nodes)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TransformationResult):
            return False

        if self.transformed_node != other.transformed_node:
            return False

        if self.changed != other.changed:
            return False

        if len(self.removed_nodes) != len(other.removed_nodes):
            return False

        unfound_other_removed_node_ids: Set[int] = {
            id(other_removed_node)
            for other_removed_node in other.removed_nodes
        }
        for removed_node in self.removed_nodes:
            try:
                removed_node_id: int = id(removed_node)
                unfound_other_removed_node_ids.remove(removed_node_id)
            except KeyError:
                return False

        return True
