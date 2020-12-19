"""A node in a tree."""
import collections
from typing import Iterable, Iterator, List, Optional, Set, Type, Union

from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException


class Node():
    """A node in a tree."""
    def __init__(self, parent: Optional['Node'] = None):
        self.parent: Optional['Node'] = parent

    def iterate_children(self) -> 'NodeIterator':  # pylint: disable=no-self-use
        """Yield children of this node."""
        nodes: NodeList = []
        return iter(nodes)

    def assert_is_type(self, node_types: Union['NodeType', 'NodeTypes']) -> None:
        """Raise an exception if type of the node is not one of the given node types."""
        is_type: bool

        if isinstance(node_types, collections.Iterable):
            is_type = any(issubclass(self.__class__, node_type) for node_type in node_types)
        else:
            is_type = issubclass(self.__class__, node_types)

        if not is_type:
            raise UnexpectedNodeTypeException()


NodeType = Type[Node]
NodeTypes = Iterable[NodeType]
NodeTypeSet = Set[NodeType]
NodeIterator = Iterator[Node]
NodeList = List[Node]
