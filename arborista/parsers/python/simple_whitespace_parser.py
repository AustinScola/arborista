"""Parser for simple whitespace."""
import libcst

from arborista.nodes.python.simple_whitespace import SimpleWhitespace
from arborista.parser import Parser

LibcstSimpleWhitespace = libcst.SimpleWhitespace


class SimpleWhitespaceParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for simple whitespace."""
    @staticmethod
    def parse_simple_whitespace(
            libcst_simple_whitespace: LibcstSimpleWhitespace) -> SimpleWhitespace:
        """Parse simple whitespace."""
        value: str = libcst_simple_whitespace.value

        simple_whitespace: SimpleWhitespace = SimpleWhitespace(value)

        return simple_whitespace
