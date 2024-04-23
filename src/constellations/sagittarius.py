"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

star_names = create_star_dictionary(['alpha',
                                     'beta^1',
                                     'beta^2',
                                     'gamma^1',
                                     'gamma^2',
                                     'delta',
                                     'epsilon',
                                     'zeta',
                                     'eta',
                                     'theta^1',
                                     'theta^2',
                                     'iota',
                                     'kappa^1',
                                     'kappa^2',
                                     'lambda',
                                     'mu',
                                     'nu^1',
                                     'nu^2',
                                     'xi^1',
                                     'xi^2',
                                     'o',
                                     'pi',
                                     'rho^1',
                                     'rho^2',
                                     'sigma',
                                     'tau',
                                     'upsilon',
                                     'phi',
                                     'chi^1',
                                     'chi^2',
                                     'chi^3',
                                     'psi',
                                     'omega'])

print(star_names)

star_names = {}

sagittarius_coordinates = array([
])

draw_lines = get_reverse_map(
    [], star_names)

constellations(coordinates=sagittarius_coordinates, star_names=star_names, constellation_name='',
               short_name='sag', line_coordinates=draw_lines, turn_half=True)
