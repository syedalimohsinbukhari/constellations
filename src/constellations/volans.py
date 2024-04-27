"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa'}

volans_coordinates = array([('09:02:26.79592', '-66:23:45.8727'), ('08:25:44.19472', '-66:08:12.8050'),
                            ('07:08:42.37030', '-70:29:49.5270'), ('07:16:49.82387', '-67:57:25.7484'),
                            ('08:07:55.79450', '-68:37:01.4330'), ('07:41:49.26100', '-72:36:21.9566'),
                            ('08:22:04.45155', '-73:23:59.9258'), ('08:39:05.16145', '-70:23:12.2826'),
                            ('06:51:26.98552', '-70:57:48.2766'), ('08:19:48.96447', '-71:30:53.6692')])

draw_lines = get_reverse_map([('alpha', 'beta'), ('beta', 'epsilon'), ('epsilon', 'alpha'), ('epsilon', 'delta'),
                              ('delta', 'gamma'), ('gamma', 'epsilon')], star_names)

constellations(coordinates=volans_coordinates, star_names=star_names, constellation_name='volans',
               short_name='vol', line_coordinates=draw_lines, turn_half=True)
