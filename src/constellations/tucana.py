"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

star_names = create_star_dictionary([])

print(star_names)

star_names = {}

tucana_coordinates = array([
                            ])

draw_lines = get_reverse_map(
    [], star_names)

constellations(coordinates=tucana_coordinates, star_names=star_names, constellation_name='tucana',
               short_name='tuc', line_coordinates=draw_lines,turn_half=True )
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()