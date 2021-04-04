"""Parse an uppercase letter."""
from typing import cast

from seligimus.characters.uppercase_letters import not_uppercase_letter

from arborista.exceptions.nebnf_syntax_error import NEBNFSyntaxError
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter, UppercaseLetterValue


def parse_uppercase_letter(string: str) -> UppercaseLetter:
    """Parse an uppercase letter."""
    if not_uppercase_letter(string):
        raise NEBNFSyntaxError(
            'The parser expected an uppercase letter but the character was not one.')
    uppercase_letter_value: UppercaseLetterValue = cast(UppercaseLetterValue, string)

    return UppercaseLetter(uppercase_letter_value)
