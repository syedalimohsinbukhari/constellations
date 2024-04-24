"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa^1', 'kappa^2', 'lambda^1',
#      'lambda^2', 'mu', 'xi', 'pi', 'sigma', 'tau']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa^1', 10: 'kappa^2', 11: 'lambda^1', 12: 'lambda^2', 13: 'mu', 14: 'xi', 15: 'pi', 16: 'sigma',
              17: 'tau'}

sculptor_coordinates = array([
])

draw_lines = get_reverse_map(
    [('alpha', 'iota'),
     ('iota', 'delta'),
     ('delta', 'gamma'),
     ('gamma', 'beta')
     ], star_names)

constellations(coordinates=sculptor_coordinates, star_names=star_names, constellation_name='',
               short_name='scl', line_coordinates=draw_lines, turn_half=True)
