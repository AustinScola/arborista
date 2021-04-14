"""A Named Extended Backus-Naur Form node."""
from abc import ABC
from typing import Any

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node


class NEBNFNode(Node, ABC):
    """A Named Extended Backus-Naur Form node."""
    @equal_type
    @equal_instance_attributes(excludes={'parent'})
    def __eq__(self, other: Any) -> bool:
        return True
