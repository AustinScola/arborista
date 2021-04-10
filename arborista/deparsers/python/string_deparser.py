"""Deparser for a Python string."""
from typing import cast

from arborista.deparser import Deparser
from arborista.deparsers.python.double_quoted_long_string_deparser import \
    DoubleQuotedLongStringDeparser
from arborista.deparsers.python.double_quoted_short_string_deparser import \
    DoubleQuotedShortStringDeparser
from arborista.deparsers.python.single_quoted_long_string_deparser import \
    SingleQuotedLongStringDeparser
from arborista.deparsers.python.single_quoted_short_string_deparser import \
    SingleQuotedShortStringDeparser
from arborista.nodes.python.double_quoted_long_string import DoubleQuotedLongString
from arborista.nodes.python.double_quoted_short_string import DoubleQuotedShortString
from arborista.nodes.python.single_quoted_long_string import SingleQuotedLongString
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String


class StringDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python string."""
    @staticmethod
    def deparse_string(string: String) -> str:
        """Return a string from a Python string node."""
        deparsed_string: str
        if isinstance(string.value, SingleQuotedShortString):
            single_quoted_short_string: SingleQuotedShortString = string.value
            deparsed_string = SingleQuotedShortStringDeparser.deparse_single_quoted_short_string(
                single_quoted_short_string)
        elif isinstance(string.value, DoubleQuotedShortString):
            double_quoted_short_string: DoubleQuotedShortString = string.value
            deparsed_string = DoubleQuotedShortStringDeparser.deparse_double_quoted_short_string(
                double_quoted_short_string)
        elif isinstance(string.value, SingleQuotedLongString):
            single_quoted_long_string: SingleQuotedLongString = string.value
            deparsed_string = SingleQuotedLongStringDeparser.deparse_single_quoted_long_string(
                single_quoted_long_string)
        else:
            double_quoted_long_string: DoubleQuotedLongString = cast(DoubleQuotedLongString,
                                                                     string.value)
            deparsed_string = DoubleQuotedLongStringDeparser.deparse_double_quoted_long_string(
                double_quoted_long_string)

        return deparsed_string
