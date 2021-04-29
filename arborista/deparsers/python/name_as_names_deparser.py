"""A deparser for Python name as names."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.name_as_name_deparser import NameAsNameDeparser
from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames


class NameAsNamesDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python name as names."""
    @staticmethod
    def deparse_name_as_names(name_as_names: NameAsNames) -> str:
        """Deparser a Python name as names."""
        string: str

        first: NameAsName = name_as_names.first
        first_string: str = NameAsNameDeparser.deparse_name_as_name(first)

        rest: List[NameAsName] = name_as_names.rest
        rest_strings = (NameAsNameDeparser.deparse_name_as_name(name_as_name)
                        for name_as_name in rest)

        string = first_string + ''.join(', ' + name_as_name_string
                                        for name_as_name_string in rest_strings)

        return string
