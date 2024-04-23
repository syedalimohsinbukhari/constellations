"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

star_names = create_star_dictionary([])

print(star_names)

star_names = {}

triangulum_australe_coordinates = array([
                            ])

draw_lines = get_reverse_map(
    [], star_names)

constellations(coordinates=triangulum_australe_coordinates, star_names=star_names, constellation_name='triangulum_australe',
               short_name='tra', line_coordinates=draw_lines,turn_half=True )
