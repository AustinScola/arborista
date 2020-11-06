"""A Python name."""
from arborista.nodes.python.statement import Statement


class Name(Statement):  # pylint: disable=too-few-public-methods
    """A Python name."""
    def __init__(self, value: str):
        self.value: str = value
