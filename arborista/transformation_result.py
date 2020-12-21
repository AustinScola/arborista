"""The result of a transformation."""
from typing import Optional

from arborista.node import Node, NodeIterable, NodeList


class TransformationResult():  # pylint: disable=too-few-public-methods
    """The result of a transformation."""
    def __init__(self, transformed_node: Optional[Node], changed: bool,
                 removed_nodes: NodeIterable):
        self.transformed_node: Optional[Node] = transformed_node
        self.changed: bool = changed
        self.removed_nodes: NodeList = list(removed_nodes)
