"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta^1', 'delta^2', 'delta^3', 'epsilon', 'zeta', 'eta', 'theta^1', 'theta^2', 'iota',
#      'kappa^1', 'kappa^2', 'lambda', 'mu', 'nu', 'xi', 'o', 'pi', 'rho', 'sigma^1', 'sigma^2', 'tau', 'upsilon',
#      'phi', 'chi', 'psi', 'omega^1', 'omega^2']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta^1', 4: 'delta^2', 5: 'delta^3', 6: 'epsilon', 7: 'zeta',
              8: 'eta', 9: 'theta^1', 10: 'theta^2', 11: 'iota', 12: 'kappa^1', 13: 'kappa^2', 14: 'lambda', 15: 'mu',
              16: 'nu', 17: 'xi', 18: 'o', 19: 'pi', 20: 'rho', 21: 'sigma^1', 22: 'sigma^2', 23: 'tau', 24: 'upsilon',
              25: 'phi', 26: 'chi', 27: 'psi', 28: 'omega^1', 29: 'omega^2'}

taurus_coordinates = array([
])

draw_lines = get_reverse_map(
    [('beta', 'epsilon'), ('epsilon', 'delta^1'), ('delta^1', 'delta^2'), ('delta^2', 'gamma'), ('zeta', 'alpha'),
     ('alpha', 'theta'), ('theta', 'gamma'), ('gamma', 'lambda'), ('lambda', 'xi'), ('xi', 'nu')], star_names)

constellations(coordinates=taurus_coordinates, star_names=star_names, constellation_name='taurus',
               short_name='tau', line_coordinates=draw_lines, turn_half=True)
