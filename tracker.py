from .coordinates import Coordinates
from typing import List
import csv

# TODO: Implementar método estático load, para transformar o csv em objeto novamente!

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

    def save_coordinates(self, path: str) -> None:
        with open(path,'w') as csv_file:
            fieldnames = ['x', 'y', 'timestamp']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
            writer.writeheader()

            for coordinate in self._coordinates:
                writer.writerow({
                    'x': str(coordinate.x),
                    'y': str(coordinate.y),
                    'timestamp': str(coordinate.timestamp)
                })
