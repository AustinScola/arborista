"""A deparser for Python dotted name as name."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.dotted_name_deparser import DottedNameDeparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.name import Name


class DottedNameAsNameDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python dotted name as name."""
    @staticmethod
    def deparse_dotted_name_as_name(dotted_name_as_name: DottedNameAsName) -> str:
        """Deparser a Python dotted name as name."""
        string: str

        dotted_name: DottedName = dotted_name_as_name.dotted_name
        dotted_name_string: str = DottedNameDeparser.deparse_dotted_name(dotted_name)

        name: Optional[Name] = dotted_name_as_name.name
        if name is not None:
            name_string: str = NameDeparser.deparse_name(name)
            string = f'{dotted_name_string} as {name_string}'
        else:
            string = dotted_name_string

        return string
