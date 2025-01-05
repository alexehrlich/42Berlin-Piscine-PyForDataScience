class calculator:
    """Calculator which can add and subtract vectors and build the dot product"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        dp = 0
        for a, b in zip(V1, V2):
            dp += a * b
        print(f"Dot product is: {dp}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        vec = []
        for a, b in zip(V1, V2):
            vec.append(a + b)
        print(f"Add Vector is: {vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        vec = []
        for a, b in zip(V1, V2):
            vec.append(a - b)
        print(f"Sous Vector is: {vec}")
