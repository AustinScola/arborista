"""A Parser for Python dotted name as names."""
from typing import List

import libcst

from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.parser import Parser
from arborista.parsers.python.dotted_name_as_name_parser import DottedNameAsNameParser

LibcstDottedNameAsNames = List[libcst.ImportAlias]


class DottedNameAsNamesParser(Parser):  # pylint: disable=too-few-public-methods
    """A Parser for Python dotted name as names."""
    @staticmethod
    def parse_dotted_name_as_names(
            libcst_dotted_name_as_names: LibcstDottedNameAsNames) -> DottedNameAsNames:
        """Parse a Python dotted name as names."""
        first_dotted_name_as_name: DottedNameAsName = \
            DottedNameAsNameParser.parse_dotted_name_as_name(libcst_dotted_name_as_names[0])
        rest_of_dotted_name_as_name: List[DottedNameAsName] = [
            DottedNameAsNameParser.parse_dotted_name_as_name(libcst_dotted_name_as_name)
            for libcst_dotted_name_as_name in libcst_dotted_name_as_names[1:]
        ]

        dotted_name_as_names: DottedNameAsNames = DottedNameAsNames(first_dotted_name_as_name,
                                                                    rest_of_dotted_name_as_name)
        return dotted_name_as_names
