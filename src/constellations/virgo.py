"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
#      'o', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'o', 15: 'pi', 16: 'rho', 17: 'sigma',
              18: 'tau', 19: 'upsilon', 20: 'phi', 21: 'chi', 22: 'psi', 23: 'omega'}

virgo_coordinates = array([
])

draw_lines = get_reverse_map(
    [('tau', 'zeta'), ('zeta', 'iota'), ('iota', 'mu'), ('zeta', 'gamma'), ('gamma', 'theta'), ('theta', 'alpha'),
     ('gamma', 'delta'), ('delta', 'epsilon'), ('gamma', 'eta'), ('eta', 'beta'), ('beta', 'nu'), ('nu', 'o'),
     ('o', 'eta')
     ], star_names)

constellations(coordinates=virgo_coordinates, star_names=star_names, constellation_name='virgo',
               short_name='vir', line_coordinates=draw_lines, turn_half=True)
