"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']
#                                     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta'}

scutum_coordinates = array([
])

draw_lines = get_reverse_map(
    [('beta', 'alpha'),
     ('alpha', 'gamma'),
     ('gamma', 'delta'),
     ('delta', 'epsilon'),
     ('epsilon', 'beta')
     ], star_names)

constellations(coordinates=scutum_coordinates, star_names=star_names, constellation_name='scutum',
               short_name='sct', line_coordinates=draw_lines, turn_half=True)
