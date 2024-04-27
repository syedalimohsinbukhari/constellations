"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa'}

triangulum_australe_coordinates = array([
    ('16:48:39.89508', '-69:01:39.7626'),
    ('15:55:08.56206', '-63:25:50.6155'),
    ('15:18:54.58198', '-68:40:46.3654'),
    ('16:15:26.26978', '-63:41:08.4492'),
    ('15:36:43.22223', '-66:19:01.3334'),
    ('16:28:28.14362', '-70:05:03.8419'),
    ('16:41:23.10722', '-68:17:46.0412'),
    ('16:35:44.81924', '-65:29:43.4478'),
    ('16:27:57.34498', '-64:03:28.5964'),
    ('15:55:29.59831', '-68:36:10.8101')
])

draw_lines = get_reverse_map(
[('beta', 'gamma'), ('gamma', 'eta'), ('eta', 'beta')], star_names)

constellations(coordinates=triangulum_australe_coordinates, star_names=star_names,
               constellation_name='triangulum_australe',
short_name = 'tra', line_coordinates = draw_lines, turn_half = True)
