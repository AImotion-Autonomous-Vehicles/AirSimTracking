# VehicleTracking

This module is responsible for keeping tracking of any kind of vehicles. The abstract class Tracker could be implemented in any application, it's just a pre-determined frame ("contract to other modules to use it"). Which is the case of the TrackerMap, a concrete class, to stream the vehicle position to a top view 2D map. The component is only responsible for keeping track of the position of the vehicle in a image, if you want to visualize the map, it's your responsibility to plot it somehow.

### Usage Example:

```python
from VehicleTracker import TrackerMap, Coordinates

initial_position = Coordinates(0,0)
tracker = TrackerMap(initial_position)

while True:
    # get position

    tracker.update_coordinates(current_position)

    tracker_map = track.get_map()

    # plot map
```