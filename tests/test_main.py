"""Test arborista.main."""
import argparse
import logging
from typing import Any, Dict, List, Union
from unittest.mock import mock_open, patch

import pytest

import arborista.main
from arborista.main import (_parse_arguments, _run_arborista, _set_up_argument_parser,
                            _set_up_logging, main)


def test_set_up_logging() -> None:
    """Test arborista.main._set_up_logging."""
    _set_up_logging()

    _assert_logger_is_set_up()


def _assert_logger_is_set_up() -> None:
    """Assert that the logger is set up with a stream handler and the correct level."""
    logger = logging.getLogger(arborista.main.__package__)

    _assert_logger_has_stream_handler(logger)
    _assert_logger_level_is_info(logger)


def _assert_logger_has_stream_handler(logger: logging.Logger) -> None:
    """Assert the logger has a single stream handler."""
    assert len(logger.handlers) == 1
    first_handler = logger.handlers[0]
    assert isinstance(first_handler, logging.StreamHandler)


def _assert_logger_level_is_info(logger: logging.Logger) -> None:
    """Assert the logger level is info."""
    assert logger.level == logging.INFO


def test_set_up_argument_parser() -> None:
    """Test arborista.main._set_up_argument_parser."""
    argument_parser: argparse.ArgumentParser = _set_up_argument_parser()

    _assert_argument_parser_is_set_up(argument_parser)


def _assert_argument_parser_is_set_up(argument_parser: argparse.ArgumentParser) -> None:
    """Assert the argument parser description and prog match the expected values."""
    _assert_argument_parser_description(argument_parser)
    _assert_argument_parser_prog(argument_parser)
    _assert_argument_parser_arguments(argument_parser)


def _assert_argument_parser_description(argument_parser: argparse.ArgumentParser) -> None:
    """Assert the argument parser description matches the expected value."""
    assert argument_parser.description == 'A tree transformation tool.'


def _assert_argument_parser_prog(argument_parser: argparse.ArgumentParser) -> None:
    """Assert the argument parser prog matches the expected value."""
    assert argument_parser.prog == 'python3 -m arborista'


def _assert_argument_parser_arguments(argument_parser: argparse.ArgumentParser) -> None:
    """Assert the argument parser arguments match the expected arguments."""
    arguments: List[argparse.Action] = argument_parser._get_positional_actions()  # pylint: disable=protected-access

    _assert_arguemnt_parser_number_of_arguments(arguments)

    file_argument: argparse.Action = arguments[0]

    _assert_file_argument_is_set_up(file_argument)


def _assert_arguemnt_parser_number_of_arguments(arguments: List[argparse.Action]) -> None:
    """Assert that the argument parser has the expected number of arguments."""
    assert len(arguments) == 1


def _assert_file_argument_is_set_up(file_argument: argparse.Action) -> None:
    """Assert that the file argument is set up."""
    _assert_file_argument_dest(file_argument)
    _assert_file_argument_help(file_argument)


def _assert_file_argument_dest(file_argument: argparse.Action) -> None:
    """Assert that the file argument has the expected destination."""
    assert file_argument.dest == 'file'


def _assert_file_argument_help(file_argument: argparse.Action) -> None:
    """Assert that the file argument has the expected help."""
    assert file_argument.help == 'file to process'


def argument_parser_from_dict(dictionary: Dict[str, Any]) -> argparse.ArgumentParser:
    """Return an argument parser from a dictionary specification."""
    argument_parser = argparse.ArgumentParser()

    try:
        for argument in dictionary['arguments']:
            name_or_flags: Union[str, List[str]] = argument['name_or_flags']
            if isinstance(name_or_flags, str):
                name: str = name_or_flags
                argument_parser.add_argument(name)
            else:
                flags: List[str] = name_or_flags
                argument_parser.add_argument(*flags)
    except KeyError:
        pass

    return argument_parser


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('argument_parser, arguments, expected_parsed_arguments', [
    (argument_parser_from_dict({}), [], argparse.Namespace()),
    (argument_parser_from_dict({'arguments': [{'name_or_flags': 'foo'}]}), ['1'], argparse.Namespace(foo='1')),
    (argument_parser_from_dict({'arguments': [{'name_or_flags': ['--foo', '-f']}]}), [], argparse.Namespace(foo=None)),
    (argument_parser_from_dict({'arguments': [{'name_or_flags': ['--foo', '-f']}]}), ['--foo', '1'], argparse.Namespace(foo='1')),
])
# yapf: enable # pylint: disable=enable-too-long
def test_parse_arguments(argument_parser: argparse.ArgumentParser, arguments: List[str],
                         expected_parsed_arguments: argparse.Namespace) -> None:
    """Test arborista.main._parse_arguments."""
    parsed_arguments: argparse.Namespace = _parse_arguments(argument_parser, arguments)

    assert parsed_arguments == expected_parsed_arguments


# yapf: disable
@pytest.mark.parametrize('parsed_arguments, file_contents, expected_file_contents_after', [
    (argparse.Namespace(file='foo.py'), '', ''),
    (argparse.Namespace(file='foo.py'), 'def f():return; return\n', 'def f():return\n'),
])
# yapf: enable
def test_run_arborista(parsed_arguments: argparse.Namespace, file_contents: str,
                       expected_file_contents_after: str) -> None:
    """Test arborista.main.test_run_arborista."""
    with patch('builtins.open', mock_open(read_data=file_contents)) as open_mock:

        _run_arborista(parsed_arguments)

        mock_file = open_mock()
        mock_file.write.assert_called_once_with(expected_file_contents_after)


# yapf: disable
@pytest.mark.parametrize('argument_parser, parsed_arguments, arguments', [
    (argument_parser_from_dict({}), argparse.Namespace(), []),
])
# yapf: enable
def test_main(argument_parser: argparse.ArgumentParser, parsed_arguments: argparse.Namespace,
              arguments: List[str]) -> None:
    """Test arborista.main.main."""
    with patch('arborista.main._set_up_argument_parser', return_value=argument_parser) as \
        set_up_argument_parser_mock, \
        patch('arborista.main._parse_arguments', return_value=parsed_arguments) as \
        parse_arguments_mock, \
        patch('arborista.main._set_up_logging') as set_up_logging_mock, \
        patch('arborista.main._run_arborista') as run_arborista_mock:

        return_value: int = main(arguments)

        _assert_main_return_value(return_value)

        set_up_argument_parser_mock.assert_called_once()
        parse_arguments_mock.assert_called_once_with(argument_parser, arguments)
        set_up_logging_mock.assert_called_once()
        run_arborista_mock.assert_called_once()


def _assert_main_return_value(return_value: int) -> None:
    """Assert that the main function returns 0."""
    assert return_value == 0
