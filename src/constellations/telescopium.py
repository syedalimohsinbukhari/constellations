"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'delta^1', 'delta^2', 'epsilon', 'zeta', 'eta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'rho', 'tau']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'delta^1', 2: 'delta^2', 3: 'epsilon', 4: 'zeta', 5: 'eta', 6: 'iota', 7: 'kappa',
              8: 'lambda', 9: 'mu', 10: 'nu', 11: 'xi', 12: 'rho', 13: 'tau'}

telescopium_coordinates = array([
])

draw_lines = get_reverse_map(
    [('zeta', 'alpha'), ('alpha', 'epsilon')], star_names)

constellations(coordinates=telescopium_coordinates, star_names=star_names, constellation_name='telescopium',
               short_name='tel', line_coordinates=draw_lines, turn_half=True)
