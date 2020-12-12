"""Nodes used for testing."""
from arborista.node import Node


class Animal(Node):
    """An animal."""


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
