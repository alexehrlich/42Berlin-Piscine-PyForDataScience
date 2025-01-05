class calculator:
    """Calculator which can perform addition,
    multiplication, subtraction, division"""
    def __init__(self, vec: list):
        self.vec = vec

    def __add__(self, object) -> None:
        self.vec = [x + object for x in self.vec]
        print(self.vec)

    def __mul__(self, object) -> None:
        self.vec = [x * object for x in self.vec]
        print(self.vec)

    def __sub__(self, object) -> None:
        self.vec = [x - object for x in self.vec]
        print(self.vec)

    def __truediv__(self, object) -> None:
        self.vec = [x / object for x in self.vec]
        print(self.vec)
