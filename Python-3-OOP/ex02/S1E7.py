from S1E9 import Character
from typing import Self


class Baratheon(Character):
    """Representing the Baratheon familiy"""
    def __init__(self, first_name, is_alive=True):
        """Initializing a Baratheon character"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Changes helat status form True to false"""
        self.is_alive = False

    def __str__(self):
        """Object as string"""
        return f"Vector:('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Object represented as string"""
        return f"Vector:('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister familiy"""
    def __init__(self, first_name, is_alive=True):
        """Initializing a Lannister character"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """Changes helat status form True to false"""
        self.is_alive = False

    def __str__(self):
        """Object as string"""
        return f"Vector:('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def __repr__(self):
        """Object represented as string"""
        return f"Vector:('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True) -> Self:
        """Creating a new Lannister"""
        return Lannister(first_name, is_alive)
