from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Class Character"""
    def __init__(self, first_name, is_alive=True):
        """Initializes abstract class with first name and health state."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method."""
        pass


class Stark(Character):
    """Stark class inherits from abstract class Character"""
    def __init__(self, first_name, is_alive=True):
        """calls the super init from abstarct class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Changes helat status form True to false"""
        self.is_alive = False
