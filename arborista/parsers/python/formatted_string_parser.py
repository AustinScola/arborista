"""Parser for a Python formatted string."""
import libcst

from arborista.parser import Parser

LibcstFormattedString = libcst.FormattedString


class FormattedStringParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python formatted string."""
