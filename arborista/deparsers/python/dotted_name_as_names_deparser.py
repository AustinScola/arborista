"""A deparser for Python dotted name as names."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.dotted_name_as_name_deparser import DottedNameAsNameDeparser
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames


class DottedNameAsNamesDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python dotted name as names."""
    @staticmethod
    def deparse_dotted_name_as_names(dotted_name_as_names: DottedNameAsNames) -> str:
        """Deparser a Python dotted name as names."""
        string: str

        first: DottedNameAsName = dotted_name_as_names.first_dotted_name_as_name
        first_string: str = DottedNameAsNameDeparser.deparse_dotted_name_as_name(first)

        rest: List[DottedNameAsName] = dotted_name_as_names.rest_of_dotted_name_as_names
        rest_strings = (DottedNameAsNameDeparser.deparse_dotted_name_as_name(dotted_name_as_name)
                        for dotted_name_as_name in rest)

        string = first_string + ''.join(', ' + name_as_name_string
                                        for name_as_name_string in rest_strings)

        return string
