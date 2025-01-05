from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King inhertis both from Baratheon and Lannister"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializing the King"""
        super().__init__(first_name, is_alive)

    def set_hairs(self, tone: str):
        """set hair tone"""
        self.hairs = tone

    def set_eyes(self, color: str):
        """set eye color"""
        self.eyes = color

    def get_hairs(self) -> str:
        """get hair tone"""
        return self.hairs

    def get_eyes(self) -> str:
        """get eye color"""
        return self.eyes
