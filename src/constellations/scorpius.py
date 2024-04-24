"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'delta', 'epsilon', 'zeta^1', 'zeta^2', 'eta_theta', 'iota^1', 'iota^2', 'kappa', 'lambda',
#      'mu^1', 'mu^2', 'nu', 'xi', 'o', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'chi', 'psi', 'omega^1', 'omega^2',
#      'G', 'H', 'N', 'Q'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'delta', 3: 'epsilon', 4: 'zeta^1', 5: 'zeta^2', 6: 'eta_theta', 7: 'iota^1',
              8: 'iota^2', 9: 'kappa', 10: 'lambda', 11: 'mu^1', 12: 'mu^2', 13: 'nu', 14: 'xi', 15: 'o', 16: 'pi',
              17: 'rho', 18: 'sigma', 19: 'tau', 20: 'upsilon', 21: 'chi', 22: 'psi', 23: 'omega^1', 24: 'omega^2',
              25: 'G', 26: 'H', 27: 'N', 28: 'Q'}

scorpius_coordinates = array([
])

draw_lines = get_reverse_map(
    [('nu', 'beta'),
     ('beta', 'omega^1'),
     ('omega^1', 'delta'),
     ('delta', 'pi'),
     ('pi', 'rho'),
     ('delta', 'sigma'),
     ('sigma', 'alpha'),
     ('alpha', 'tau'),
     ('tau', 'epsilon'),
     ('epsilon', 'mu'),
     ('mu', 'zeta^1'),
     ('zeta^1', 'zeta^2'),
     ('zeta^2', 'eta'),
     ('eta', 'theta'),
     ('theta', 'iota'),
     ('iota', 'kappa'),
     ('kappa', 'nu'),
     ('nu', 'lambda')
     ], star_names)

constellations(coordinates=scorpius_coordinates, star_names=star_names, constellation_name='',
               short_name='sco', line_coordinates=draw_lines, turn_half=True)
