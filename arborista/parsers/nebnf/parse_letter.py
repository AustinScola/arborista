"""Parse a letter."""
from typing import cast

from seligimus.characters.letters import not_letter

from arborista.exceptions.nebnf_syntax_error import NEBNFSyntaxError
from arborista.nodes.nebnf.letter import Letter, LetterValue


def parse_letter(string: str) -> Letter:
    """Parse a letter."""
    if not_letter(string):
        raise NEBNFSyntaxError('The parser expected a letter but the character was not one.')
    letter_value: LetterValue = cast(LetterValue, string)

    return Letter(letter_value)
