from abc import ABC
import numpy as np
from exceptions import OutboundCoordinates
import matplotlib.pyplot as plt

class Coordinates:

    x: int
    y: int

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __init__(self, x: int, y: int) -> None:
        self.x = int(x)
        self.y = int(y)

class Tracker(ABC):

    initial_coordinates: Coordinates
    current_coordinates: Coordinates

    def __init__(self, initial_coordinates: Coordinates) -> None:
        self.initial_coordinates = initial_coordinates
        self.current_coordinates = initial_coordinates

    def update_coordinates(self, coordinates: Coordinates) -> None:
        self.current_coordinates = coordinates

class TrackerMap(Tracker):

    __WIDTH = 900
    __HEIGHT = 900
    __CHANNELS = 1

    def __init__(self, initial_coordinates: Coordinates, height=900, width=900) -> None:
        super().__init__(initial_coordinates)
        self.__WIDTH = width
        self.__HEIGHT = height
        self._map = np.zeros((self.__HEIGHT, self.__WIDTH, self.__CHANNELS), np.uint8)

    def update_coordinates(self, coordinates: Coordinates) -> None:
        if self.__invalid_coordinates(coordinates):
            raise OutboundCoordinates

        coordinates.x = coordinates.x - self.initial_coordinates.x
        coordinates.y = coordinates.y - self.initial_coordinates.y

        print(coordinates)

        self.__update_map(coordinates)
        super().update_coordinates(coordinates)

    def __invalid_coordinates(self, coordinates: Coordinates) -> bool:
        if coordinates.x < 0 or coordinates.x >= self.__WIDTH:
            return True
        if coordinates.y < 0 or coordinates.y >= self.__HEIGHT:
            return True
        return False

    def __update_map(self, coordinates: Coordinates) -> None:
        self._map[self.current_coordinates.x, self.current_coordinates.y, 0] = 0.5
        self._map[coordinates.x, coordinates.y, 0] = 1

    def get_map(self):
        return self._map

class TrackerPlot(Tracker):
    def __init__(self, initial_coordinates: Coordinates, bounds: 100) -> None:
        super().__init__(initial_coordinates)
        self.__BOUNDS = bounds

    def update_coordinates(self, coordinates: Coordinates) -> None:
        if self.__invalid_coordinates(coordinates):
            raise OutboundCoordinates

        self.__update_plot(coordinates)
        super().update_coordinates(coordinates)

    def __invalid_coordinates(self, coordinates: Coordinates) -> bool:
        if coordinates.x < -self.__BOUNDS or coordinates.x >= self.__BOUNDS:
            return True
        if coordinates.y < -self.__BOUNDS or coordinates.y >= self.__BOUNDS:
            return True
        return False

    def __update_plot(self, coordinates: Coordinates) -> None:
        plt.scatter(coordinates.x, coordinates.y)

    def show_plot(self):
        plt.show()
