"""Parser for a Python name."""
import libcst

from arborista.nodes.python.name import Name
from arborista.parser import Parser

LibcstName = libcst.Name


class NameParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python name."""
    @staticmethod
    def parse_name(libcst_name: LibcstName) -> Name:
        """Parser a Python name."""
        value: str = libcst_name.value
        name: Name = Name(value)
        return name
