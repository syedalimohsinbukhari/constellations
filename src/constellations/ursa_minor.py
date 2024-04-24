"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'lambda', 'pi^1', 'pi^2'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'lambda',
              9: 'pi^1', 10: 'pi^2'}

ursa_minor_coordinates = array([
    ('02:31:49.09', '+89:15:50.8'),
    ('14:50:42.32580', '+74:09:19.8142'),
    ('15:20:43.71604', '+71:50:02.4596'),
    ('17:32:12.99671', '+86:35:11.2584'),
    ('16:45:58.24168', '+82:02:14.1233'),
    ('15:44:03.51892', '+77:47:40.1788'),
    ('16:17:30.27025', '+75:45:19.2351'),
    ('15:31:25.05417', '+77:20:57.6199'),
    ('17:16:56.4107', '+89:02:15.734'),
    ('15:29:11.18599', '+80:26:54.9713'),
    ('15:39:38.61131', '+79:58:59.5495')
])

draw_lines = get_reverse_map(
    [('alpha', 'delta'), ('delta', 'epsilon'), ('epsilon', 'zeta'), ('zeta', 'theta'), ('theta', 'beta'),
     ('beta', 'gamma'), ('gamma', 'eta'), ('eta', 'zeta')
     ], star_names)

constellations(coordinates=ursa_minor_coordinates, star_names=star_names, constellation_name='ursa_minor',
               short_name='umi', line_coordinates=draw_lines, turn_half=True)
