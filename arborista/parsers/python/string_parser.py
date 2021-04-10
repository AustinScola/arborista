"""Parser for a Python string."""
from typing import Optional, Union

import libcst

from arborista.nodes.python.double_quoted_long_string import DoubleQuotedLongString
from arborista.nodes.python.double_quoted_short_string import DoubleQuotedShortString
from arborista.nodes.python.single_quoted_long_string import SingleQuotedLongString
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String, StringPrefix, StringValue
from arborista.parser import Parser

LibcstString = Union[libcst.SimpleString, libcst.FormattedString]


class StringParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python string."""
    @staticmethod
    def parse_string(libcst_string: LibcstString) -> String:
        """Parse a Python string node."""
        string_prefix: Optional[StringPrefix] = None
        string_value: StringValue
        string: String

        if isinstance(libcst_string, libcst.SimpleString):
            libcst_simple_string: libcst.SimpleString = libcst_string
            if libcst_simple_string.value.startswith("'''") and libcst_simple_string.value.endswith(
                    "'''"):
                single_quoted_long_string: SingleQuotedLongString = SingleQuotedLongString(
                    libcst_simple_string.value[3:-3])
                string_value = single_quoted_long_string
            elif libcst_simple_string.value.startswith(
                    '"""') and libcst_simple_string.value.endswith('"""'):
                double_quoted_long_string: DoubleQuotedLongString = DoubleQuotedLongString(
                    libcst_simple_string.value[3:-3])
                string_value = double_quoted_long_string
            elif libcst_simple_string.value.startswith("'") and libcst_simple_string.value.endswith(
                    "'"):
                single_quoted_short_string: SingleQuotedShortString = SingleQuotedShortString(
                    libcst_simple_string.value[1:-1])
                string_value = single_quoted_short_string
            else:
                double_quoted_short_string: DoubleQuotedShortString = DoubleQuotedShortString(
                    libcst_simple_string.value[1:-1])
                string_value = double_quoted_short_string
        else:
            raise NotImplementedError  # pragma: no cover

        string = String(string_prefix, string_value)

        return string
