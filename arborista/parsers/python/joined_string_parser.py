"""Parser for a Python joined string."""
from typing import List, Union

import libcst

from arborista.nodes.python.joined_string import JoinedString
from arborista.nodes.python.string import String
from arborista.parser import Parser
from arborista.parsers.python.string_parser import LibcstString, StringParser

LibcstJoinedString = libcst.ConcatenatedString


class JoinedStringParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python joined string."""
    @staticmethod
    def parse_joined_string(libcst_joined_string: LibcstJoinedString) -> JoinedString:
        """Parse a Python joined string."""
        strings: List[String] = []

        while True:
            libcst_left_string: LibcstString = libcst_joined_string.left

            left_string: String = StringParser.parse_string(libcst_left_string)
            strings.append(left_string)

            libcst_right_string: Union[LibcstString,
                                       LibcstJoinedString] = libcst_joined_string.right
            if isinstance(libcst_right_string, LibcstJoinedString):
                libcst_joined_string = libcst_right_string
                continue

            right_string: String = StringParser.parse_string(libcst_right_string)
            strings.append(right_string)
            break

        joined_string: JoinedString = JoinedString(strings)
        return joined_string
