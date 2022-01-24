from typing import List
import matplotlib.pyplot as plt
from .coordinates import Coordinates

class CartesianPlane:

    def __init__(self) -> None:
        self._figure = plt.gca()
        self.__set_axes()
        self._figure.grid()

    def __set_axes(self):
        self._figure.spines['top'].set_color('none')
        self._figure.spines['bottom'].set_position('zero')
        self._figure.spines['left'].set_position('zero')
        self._figure.spines['right'].set_color('none')

    def plot_coordinates(self, coordinates: List[Coordinates]) -> None:
        x_points = self.__get_x_points(coordinates)
        y_points = self.__get_y_points(coordinates)

        self._figure.plot(x_points, y_points, '-o', color='black')
        plt.show()

    def __get_x_points(self, coordinates: List[Coordinates]) -> List[float]:
        return [point.x for point in coordinates]

    def __get_y_points(self, coordinates: List[Coordinates]) -> List[float]:
        return [point.y for point in coordinates]
