from typing import List

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

class Tracker:

    _initial_coordinates: Coordinates
    _coordinates: List[Coordinates]

    def __init__(self, initial_coordinates: Coordinates) -> None:
        self._initial_coordinates = initial_coordinates
        self._coordinates = [Coordinates(0.0,0.0)]

    def update_coordinates(self, coordinates: Coordinates) -> None:
        coordinates.x -= self._initial_coordinates.x
        coordinates.y -= self._initial_coordinates.y

        if coordinates == self._coordinates[len(self._coordinates)-1]:
            return

        self._coordinates.append(coordinates)

    def get_coordinates(self) -> List[Coordinates]:
        return self._coordinates
