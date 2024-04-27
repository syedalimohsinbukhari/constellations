"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta^1', 2: 'beta^2', 3: 'beta^3', 4: 'gamma', 5: 'delta', 6: 'epsilon', 7: 'zeta',
              8: 'eta', 9: 'theta', 10: 'iota', 11: 'kappa', 12: 'lambda^1', 13: 'lambda^2', 14: 'mu', 15: 'nu',
              16: 'pi', 17: 'rho'}

tucana_coordinates = array([
])

draw_lines = get_reverse_map(
    [('gamma', 'alpha'), ('alpha', 'delta'), ('delta', 'epsilon'), ('epsilon', 'zeta'), ('zeta', 'beta'),
     ('beta', 'gamma')], star_names)

constellations(coordinates=tucana_coordinates, star_names=star_names, constellation_name='tucana',
               short_name='tuc', line_coordinates=draw_lines, turn_half=True)
