"""Test arborista.parsers.nebnf.parse_uppercase_letter."""
from typing import Union

import pytest

from arborista.exceptions.nebnf_syntax_error import NEBNFSyntaxError
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter
from arborista.parsers.nebnf.parse_uppercase_letter import parse_uppercase_letter


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('string, expected_result', [
    ('A', UppercaseLetter('A')),
    ('B', UppercaseLetter('B')),
    ('Z', UppercaseLetter('Z')),
    ('a', NEBNFSyntaxError('The parser expected an uppercase letter but the character was not one.')),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_uppercase_letter(string: str, expected_result: Union[UppercaseLetter,
                                                                    Exception]) -> None:
    """Test arborista.parsers.nebnf.parse_uppercase_letter.parse_uppercase_letter"""
    if isinstance(expected_result, Exception):
        expected_exception: Exception = expected_result
        with pytest.raises(type(expected_exception), match=str(expected_exception)):
            parse_uppercase_letter(string)
    else:
        expected_uppercase_letter: UppercaseLetter = expected_result
        uppercase_letter: UppercaseLetter = parse_uppercase_letter(string)

        assert uppercase_letter == expected_uppercase_letter
