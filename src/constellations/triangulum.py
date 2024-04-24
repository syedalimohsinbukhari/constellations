"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'iota'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'iota'}

triangulum_coordinates = array([
    ('01:53:04.90710', '+29:34:43.7801'),
    ('02:09:32.62712', '+34:59:14.2694'),
    ('02:17:18.86703', '+33:50:49.8950'),
    ('02:17:03.23016', '+34:13:27.2260'),
    ('02:02:57.95579', '+33:17:02.8813'),
    ('02:12:22.27970', '+30:18:11.0530')
])

draw_lines = get_reverse_map(
    [('alpha', 'beta'), ('beta', 'gamma'), ('gamma', 'alpha')], star_names)

constellations(coordinates=triangulum_coordinates, star_names=star_names, constellation_name='triangulum',
               short_name='tri', line_coordinates=draw_lines, turn_half=True)
