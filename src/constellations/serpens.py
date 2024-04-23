"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

star_names = create_star_dictionary(
    ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
     'omicron', 'pi', 'rho', 'sigma', 'tau^1', 'tau^2', 'tau^3', 'tau^4', 'tau^5', 'tau^6', 'tau^7', 'tau^8', 'upsilon',
     'phi', 'chi', 'psi', 'omega'])

print(star_names)

star_names = {}

serpens_coordinates = array([
])

draw_lines = get_reverse_map(
    [], star_names)

constellations(coordinates=serpens_coordinates, star_names=star_names, constellation_name='serpens',
               short_name='ser', line_coordinates=draw_lines, turn_half=True)
