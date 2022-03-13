import time

class Coordinates:

    x: float
    y: float
    timestamp: float

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __init__(self, x: float, y: float, timestamp=time.time()) -> None:
        self.x = float(x)
        self.y = float(y)
        self.timestamp = timestamp

    def __eq__(self, other: object) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        return False
