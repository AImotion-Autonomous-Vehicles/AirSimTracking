from typing import List

class Coordinates:

    x: int
    y: int

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __init__(self, x: int, y: int) -> None:
        self.x = int(x)
        self.y = int(y)

class Tracker:

    _initial_coordinates: Coordinates
    _coordinates: List[Coordinates]

    def __init__(self, initial_coordinates: Coordinates) -> None:
        self._initial_coordinates = initial_coordinates
        self._coordinates = [Coordinates(0,0)]

    def update_coordinates(self, coordinates: Coordinates) -> None:
        coordinates.x -= self._initial_coordinates.x
        coordinates.y -= self._initial_coordinates.y

        if coordinates.x == self._coordinates[len(self._coordinates)-1].x:
            return

        if coordinates.y == self._coordinates[len(self._coordinates)-1].y:
            return

        self._coordinates.append(coordinates)

    def get_coordinates(self) -> List[Coordinates]:
        return self._coordinates
