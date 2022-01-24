class Coordinates:

    x: float
    y: float

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other: object) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        return False
