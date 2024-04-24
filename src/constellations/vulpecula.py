"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha'])
#
# print(star_names)

star_names = {0: 'alpha'}

vulpecula_coordinates = array([('19:28:42.3299', '+24:39:53.661')])

draw_lines = get_reverse_map(
    [('alpha')], star_names)

constellations(coordinates=vulpecula_coordinates, star_names=star_names, constellation_name='vulpecula',
               short_name='vul', line_coordinates=draw_lines,turn_half=True)
