"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

star_names = create_star_dictionary(['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']
                                    )

print(star_names)

star_names = {}

scutum_coordinates = array([
])

draw_lines = get_reverse_map(
    [], star_names)

constellations(coordinates=scutum_coordinates, star_names=star_names, constellation_name='scutum',
               short_name='scu', line_coordinates=draw_lines, turn_half=True)
