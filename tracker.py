from typing import List
from .coordinates import Coordinates

class Tracker:

    _initial_coordinates: Coordinates
    _coordinates: List[Coordinates]

    def __init__(self, initial_coordinates: Coordinates) -> None:
        self._initial_coordinates = initial_coordinates
        self._coordinates = [Coordinates(0.0,0.0)]

    def update_coordinates(self, coordinates: Coordinates) -> None:
        coordinates.x -= self._initial_coordinates.x
        coordinates.y -= self._initial_coordinates.y

        if coordinates == self.__get_last_coordinates():
            return

        self._coordinates.append(coordinates)

    def __get_last_coordinates(self):
        return self._coordinates[len(self._coordinates)-1]

    def get_coordinates(self) -> List[Coordinates]:
        return self._coordinates
