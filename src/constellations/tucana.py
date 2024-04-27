"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta^1', 2: 'beta^2', 3: 'beta^3', 4: 'gamma', 5: 'delta', 6: 'epsilon', 7: 'zeta',
              8: 'eta', 9: 'theta', 10: 'iota', 11: 'kappa', 12: 'lambda^1_A', 13: 'lambda^1_B', 14: 'lambda^2',
              15: 'nu', 16: 'pi', 17: 'rho'}

tucana_coordinates = array([('22:18:30.11244', '-60:15:34.66640'), ('00:31:32.67090', '-62:57:29.58700'),
                            ('00:31:33.42230', '-62:57:56.13400'), ('00:32:43.80000', '-63:01:52.00000'),
                            ('23:17:25.77222', '-58:14:08.62870'), ('22:27:19.96745', '-64:57:58.87750'),
                            ('23:59:54.97761', '-65:34:37.68040'),
                            ('00:20:04.25995', '-64:52:29.25490'), ('23:57:35.07852', '-64:17:53.62290'),
                            ('00:33:23.35876', '-71:15:58.49040'), ('01:07:18.66365', '-61:46:31.04340'),
                            ('01:15:46.16226', '-68:52:33.33560'), ('00:52:24.51980', '-69:30:13.54400'),
                            ('00:52:28.34870', '-69:30:10.38190'), ('00:55:00.31129', '-69:31:37.50250'),
                            ('22:33:00.06240', '-61:58:55.63900'), ('00:20:39.03682', '-69:37:29.68210'),
                            ('00:42:28.37166', '-65:28:04.91000')])

draw_lines = get_reverse_map([('gamma', 'alpha'), ('alpha', 'delta'), ('delta', 'epsilon'), ('epsilon', 'zeta'),
                              ('zeta', 'beta^1'), ('beta^1', 'gamma')], star_names)

constellations(coordinates=tucana_coordinates, star_names=star_names, constellation_name='tucana',
               short_name='tuc', line_coordinates=draw_lines, turn_half=True)
