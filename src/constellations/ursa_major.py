"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

star_names = create_star_dictionary([])

print(star_names)

star_names = {}

ursa_major_coordinates = array([
                            ])

draw_lines = get_reverse_map(
    [], star_names)

constellations(coordinates=ursa_major_coordinates, star_names=star_names, constellation_name='ursa_major',
               short_name='uma', line_coordinates=draw_lines,turn_half=True )
