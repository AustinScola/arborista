"""Test arborista.parsers.nebnf.parse_lowercase_letter."""
from typing import Union

import pytest

from arborista.exceptions.nebnf_syntax_error import NEBNFSyntaxError
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter
from arborista.parsers.nebnf.parse_lowercase_letter import parse_lowercase_letter


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('string, expected_result', [
    ('a', LowercaseLetter('a')),
    ('b', LowercaseLetter('b')),
    ('z', LowercaseLetter('z')),
    ('A', NEBNFSyntaxError('The parser expected a lowercase letter but the character was not one.')),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_lowercase_letter(string: str, expected_result: Union[LowercaseLetter,
                                                                    Exception]) -> None:
    """Test arborista.parsers.nebnf.parse_lowercase_letter.parse_lowercase_letter"""
    if isinstance(expected_result, Exception):
        expected_exception: Exception = expected_result
        with pytest.raises(type(expected_exception), match=str(expected_exception)):
            parse_lowercase_letter(string)
    else:
        expected_lowercase_letter: LowercaseLetter = expected_result
        lowercase_letter: LowercaseLetter = parse_lowercase_letter(string)

        assert lowercase_letter == expected_lowercase_letter
