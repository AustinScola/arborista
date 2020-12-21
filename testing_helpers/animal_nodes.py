"""Nodes used for testing."""
from typing import Any

from arborista.node import Node


class Animal(Node):
    """An animal."""
    def __eq__(self, other: Any) -> bool:
        equal: bool = self.__class__ == other.__class__
        return equal


class Mammal(Animal):
    """A mammal."""


class Dog(Mammal):
    """A dog."""


class Cat(Mammal):
    """A cat."""


class Bird(Animal):
    """A bird."""


class Reptile(Animal):
    """A reptile."""


class Lizard(Reptile):
    """A lizard."""
