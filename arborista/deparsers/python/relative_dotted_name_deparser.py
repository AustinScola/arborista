"""A deparser for Python dotted names."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.dotted_name_deparser import DottedNameDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.relative_dotted_name import RelativeDottedName


class RelativeDottedNameDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python dotted names."""
    @staticmethod
    def deparse_relative_dotted_name(relative_dotted_name: RelativeDottedName) -> str:
        """Deparser a Python dotted name."""
        string: str

        dots_string = '.' * relative_dotted_name.dots

        dotted_name: Optional[DottedName] = relative_dotted_name.dotted_name
        if dotted_name is None:
            string = dots_string
        else:
            dotted_name_string = DottedNameDeparser.deparse_dotted_name(dotted_name)
            string = dots_string + dotted_name_string

        return string
