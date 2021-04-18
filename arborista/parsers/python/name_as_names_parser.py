"""A parser for Python names as other names."""
from typing import List, Sequence

import libcst

from arborista.nodes.python.name_as_name import NameAsName
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.parser import Parser
from arborista.parsers.python.name_as_name_parser import LibcstNameAsName, NameAsNameParser

LibcstNameAsNames = Sequence[libcst.ImportAlias]


class NameAsNamesParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for Python names as other names."""
    @staticmethod
    def parse_name_as_names(libcst_name_as_names: LibcstNameAsNames) -> NameAsNames:
        """Parse Python names as other names."""
        first_libcst_name_as_name: LibcstNameAsName = libcst_name_as_names[0]
        first: NameAsName = NameAsNameParser.parse_name_as_name(first_libcst_name_as_name)

        rest: List[NameAsName] = [
            NameAsNameParser.parse_name_as_name(libcst_name_as_name)
            for libcst_name_as_name in libcst_name_as_names[1:]
        ]

        name_as_names: NameAsNames = NameAsNames(first, rest)
        return name_as_names
