"""A Python name."""
from arborista.nodes.python.atom import Atom


class Name(Atom):  # pylint: disable=too-few-public-methods
    """A Python name."""
    def __init__(self, value: str):
        self.value: str = value
