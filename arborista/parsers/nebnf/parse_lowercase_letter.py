"""Parse a lowercase letter."""
from typing import cast

from seligimus.characters.lowercase_letters import not_lowercase_letter

from arborista.exceptions.nebnf_syntax_error import NEBNFSyntaxError
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter, LowercaseLetterValue


def parse_lowercase_letter(string: str) -> LowercaseLetter:
    """Parse a lowercase letter."""
    if not_lowercase_letter(string):
        raise NEBNFSyntaxError(
            'The parser expected a lowercase letter but the character was not one.')
    lowercase_letter_value: LowercaseLetterValue = cast(LowercaseLetterValue, string)

    return LowercaseLetter(lowercase_letter_value)
