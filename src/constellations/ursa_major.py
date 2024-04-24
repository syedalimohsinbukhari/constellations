"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
#      'o', 'pi^1', 'pi^2', 'rho', 'sigma^1', 'sigma^2', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'o', 15: 'pi^1', 16: 'pi^2', 17: 'rho',
              18: 'sigma^1', 19: 'sigma^2', 20: 'tau', 21: 'upsilon', 22: 'phi', 23: 'chi', 24: 'psi', 25: 'omega'}

ursa_major_coordinates = array([
])

draw_lines = get_reverse_map(
    [('eta', 'zeta'), ('zeta', 'epsilon'), ('epsilon', 'delta'), ('delta', 'alpha'), ('alpha', 'beta'),
     ('beta', 'gamma'), ('gamma', 'delta'), ('alpha', 'o'), ('o', 'upsilon'), ('upsilon', 'beta'), ('gamma', 'chi'),
     ('chi', 'psi'), ('psi', 'mu'), ('mu', 'lambda'), ('chi', 'nu'), ('nu', 'xi')
     ], star_names)

constellations(coordinates=ursa_major_coordinates, star_names=star_names, constellation_name='ursa_major',
               short_name='uma', line_coordinates=draw_lines, turn_half=True)
