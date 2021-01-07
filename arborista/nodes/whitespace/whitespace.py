"""Characters that do not correspond to a mark when written."""
from abc import ABC

from arborista.node import Node


class Whitespace(Node, ABC):
    """Characters that do not correspond to a mark when written."""
