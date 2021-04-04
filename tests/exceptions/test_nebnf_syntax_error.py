"""Test arborista.exceptions.nebnf_syntax_error."""
from arborista.exception import ArboristaException
from arborista.exceptions.nebnf_syntax_error import NEBNFSyntaxError


def test_inheritance() -> None:
    """Test arborista.exceptions.nebnf_syntax_error.NEBNFSyntaxError inheritance."""
    assert issubclass(NEBNFSyntaxError, ArboristaException)
