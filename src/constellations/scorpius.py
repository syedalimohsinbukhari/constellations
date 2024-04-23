"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

star_names = create_star_dictionary(
    ['alpha', 'beta', 'delta', 'epsilon', 'zeta^1', 'zeta^2', 'eta_theta', 'iota^1', 'iota^2', 'kappa', 'lambda',
     'mu^1', 'mu^2', 'nu', 'xi', 'o', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'chi', 'psi', 'omega^1', 'omega^2',
     'G', 'H', 'N', 'Q'])

print(star_names)

star_names = {}

scorpius_coordinates = array([
])

draw_lines = get_reverse_map(
    [], star_names)

constellations(coordinates=scorpius_coordinates, star_names=star_names, constellation_name='',
               short_name='sco', line_coordinates=draw_lines, turn_half=True)
