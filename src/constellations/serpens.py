"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
#      'omicron', 'pi', 'rho', 'sigma', 'tau^1', 'tau^2', 'tau^3', 'tau^4', 'tau^5', 'tau^6', 'tau^7', 'tau^8', 'upsilon',
#      'phi', 'chi', 'psi', 'omega'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'omicron', 15: 'pi', 16: 'rho', 17: 'sigma',
              18: 'tau^1', 19: 'tau^2', 20: 'tau^3', 21: 'tau^4', 22: 'tau^5', 23: 'tau^6', 24: 'tau^7', 25: 'tau^8',
              26: 'upsilon', 27: 'phi', 28: 'chi', 29: 'psi', 30: 'omega'}

serpens_coordinates = array([
])

draw_lines = get_reverse_map(
    [('iota', 'kappa'),
     ('kappa', 'gamma'),
     ('gamma', 'beta'),
     ('beta', 'iota'),
     ('beta', 'delta'),
     ('delta', 'alpha'),
     ('alpha', 'epsilon'),
     ('epsilon', 'omega'),
     ('omega', 'mu')
     ], star_names)

constellations(coordinates=serpens_coordinates, star_names=star_names, constellation_name='serpens',
               short_name='ser1', line_coordinates=draw_lines, turn_half=True)
# its short name is not based on 3 letters