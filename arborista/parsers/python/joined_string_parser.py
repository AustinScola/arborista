"""Parser for a Python joined string."""
from typing import List, Union, cast

import libcst

from arborista.nodes.python.formatted_string import FormattedString
from arborista.nodes.python.joined_string import JoinedString
from arborista.nodes.python.simple_string import SimpleString
from arborista.parser import Parser
from arborista.parsers.python.formatted_string_parser import LibcstFormattedString
from arborista.parsers.python.simple_string_parser import LibcstSimpleString, SimpleStringParser
from arborista.parsers.python.string_parser import LibcstString

LibcstJoinedString = libcst.ConcatenatedString


class JoinedStringParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python joined string."""
    @staticmethod
    def parse_joined_string(libcst_joined_string: LibcstJoinedString) -> JoinedString:
        """Parse a Python joined string."""
        strings: List[Union[SimpleString, FormattedString]] = []

        while True:
            libcst_left_string: Union[LibcstSimpleString,
                                      LibcstFormattedString] = libcst_joined_string.left
            libcst_right_string: LibcstString = libcst_joined_string.right

            left_string: Union[SimpleString, FormattedString]
            if isinstance(libcst_left_string, LibcstSimpleString):
                libcst_simple_string: LibcstSimpleString = libcst_left_string
                simple_string: SimpleString = SimpleStringParser.parse_simple_string(
                    libcst_simple_string)
                left_string = simple_string
            else:
                raise NotImplementedError
            strings.append(left_string)

            right_string: Union[SimpleString, FormattedString]
            if isinstance(libcst_right_string, LibcstSimpleString):
                libcst_simple_string = libcst_right_string
                simple_string = SimpleStringParser.parse_simple_string(libcst_simple_string)
                right_string = simple_string
            elif isinstance(libcst_right_string, LibcstFormattedString):
                raise NotImplementedError
            else:
                libcst_joined_string = cast(LibcstJoinedString, libcst_right_string)
                continue
            strings.append(right_string)
            break

        joined_string: JoinedString = JoinedString(strings)
        return joined_string
