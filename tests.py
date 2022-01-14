from unittest import TestCase
from tracker import Tracker, Coordinates, TrackerMap
from exceptions import OutboundCoordinates

class TrackerTest(TestCase):
    def setUp(self) -> None:
        self.initial_coordinates = Coordinates(0,0)
        self.tracker = Tracker(self.initial_coordinates)

    def test_initial_coordinates(self) -> None:
        self.assertEqual(self.tracker.initial_coordinates, self.initial_coordinates)

    def test_update_current_coordinates(self) -> None:
        coordinates = Coordinates(1,1)
        self.tracker.update_coordinates(coordinates)

        self.assertEqual(self.tracker.current_coordinates, coordinates)

class TrackerMapTest(TestCase):
    def setUp(self) -> None:
        initial_coordinates = Coordinates(0,0)
        self.tracker = TrackerMap(initial_coordinates)

    def test_outbound_coordinates(self):
        with self.assertRaises(OutboundCoordinates):
            outbound_coordinates = Coordinates(10000, 10000)
            self.tracker.update_coordinates(outbound_coordinates)

    def test_inboud_coordinates(self):
        coordinates = Coordinates(899, 899)

        self.tracker.update_coordinates(coordinates)

        self.assertEqual(self.tracker.current_coordinates, coordinates)

    def test_map(self):
        initial_coordinates = Coordinates(100,200)
        current_coordinates = Coordinates(200,200)

        self.tracker.update_coordinates(initial_coordinates)
        self.tracker.update_coordinates(current_coordinates)
        map = self.tracker.get_map()

        self.assertEqual(map[initial_coordinates.x, initial_coordinates.y, 0], 127)
        self.assertEqual(map[current_coordinates.x, current_coordinates.y, 0], 255)
