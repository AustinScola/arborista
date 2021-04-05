"""Test arborista.parsers.nebnf.parse_letter."""
from typing import Union

import pytest

from arborista.exceptions.nebnf_syntax_error import NEBNFSyntaxError
from arborista.nodes.nebnf.letter import Letter
from arborista.parsers.nebnf.parse_letter import parse_letter


# yapf: disable
@pytest.mark.parametrize('string, expected_result', [
    ('a', Letter('a')),
    ('b', Letter('b')),
    ('z', Letter('z')),
    ('A', Letter('A')),
    ('$', NEBNFSyntaxError('The parser expected a letter but the character was not one.')),
])
# yapf: enable
def test_parse_letter(string: str, expected_result: Union[Letter, Exception]) -> None:
    """Test arborista.parsers.nebnf.parse_letter.parse_letter."""
    if isinstance(expected_result, Exception):
        expected_exception: Exception = expected_result
        with pytest.raises(type(expected_exception), match=str(expected_exception)):
            parse_letter(string)
    else:
        expected_letter: Letter = expected_result
        letter: Letter = parse_letter(string)

        assert letter == expected_letter
