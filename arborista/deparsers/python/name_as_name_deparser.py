"""A deparser for Python name as name."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName


class NameAsNameDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python name as name."""
    @staticmethod
    def deparse_name_as_name(name_as_name: NameAsName) -> str:
        """Deparser a Python name as name."""
        string: str

        name: Name = name_as_name.name
        name_string: str = NameDeparser.deparse_name(name)

        new_name: Optional[Name] = name_as_name.new_name
        if new_name is not None:
            new_name_string: str = NameDeparser.deparse_name(new_name)
            string = f'{name_string} as {new_name_string}'
        else:
            string = name_string

        return string
