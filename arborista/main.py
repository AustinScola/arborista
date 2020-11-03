"""Main module."""
import argparse
import logging
from typing import List

from arborista.node import Node
from arborista.transformation import Transformations
from arborista.transformer import Transformer
from arborista.tree import Tree

LOGGER = logging.getLogger(__package__)


def _set_up_logging() -> None:
    """Set up logging."""
    LOGGER.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    LOGGER.addHandler(stream_handler)


def _set_up_argument_parser() -> argparse.ArgumentParser:
    """Set up a argument parser."""
    argument_parser = argparse.ArgumentParser(prog=f'python3 -m {__package__}',
                                              description='A tree transformation tool.')
    return argument_parser


def _parse_arguments(argument_parser: argparse.ArgumentParser,
                     arguments: List[str]) -> argparse.Namespace:
    """Return parsed arguments."""
    parsed_arguments: argparse.Namespace = argument_parser.parse_args(arguments)
    return parsed_arguments


def _run_transformer() -> None:
    """Run the transformer with a set of transformations on the Python code."""
    transformations: Transformations = []
    transformer = Transformer(transformations)
    root: Node = Node()
    tree: Tree = Tree(root)
    transformer.run(tree)


def main(arguments: List[str]) -> int:
    """Main function."""
    argument_parser = _set_up_argument_parser()
    parsed_arguments: argparse.Namespace = _parse_arguments(  #pylint: disable=unused-variable
        argument_parser, arguments)
    _set_up_logging()
    _run_transformer()
    return 0
