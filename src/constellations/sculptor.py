"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa^1', 'kappa^2', 'lambda^1',
#      'lambda^2', 'mu', 'xi', 'pi', 'sigma', 'tau']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa^1', 10: 'kappa^2', 11: 'lambda^1', 12: 'lambda^2', 13: 'mu', 14: 'xi', 15: 'pi', 16: 'sigma',
              17: 'tau'}

sculptor_coordinates = array([('00:58:36.35930', '-29:21:26.8247'),
                              ('23:32:58.25898', '-37:49:05.7570'),
                              ('23:18:49.44076', '-32:31:55.2890'),
                              ('23:48:55.54658', '-28:07:48.9745'),
                              ('01:45:38.75712', '-25:03:09.4022'),
                              ('00:02:19.92035', '-29:43:13.4873'),
                              ('00:27:55.69820', '-33:00:25.7900'),
                              ('00:11:44.02079', '-35:07:59.2320'),
                              ('00:21:31.19799', '-28:58:53.2957'),
                              ('00:09:21.06696', '-27:59:16.5322'),
                              ('00:11:34.41935', '-27:47:59.0290'),
                              ('00:42:42.89190', '-38:27:48.5416'),
                              ('00:44:12.09871', '-38:25:18.0704'),
                              ('23:40:38.14898', '-32:04:23.2478'),
                              ('01:01:18.27548', '-38:54:59.5033'),
                              ('01:42:08.62230', '-32:19:37.2862'),
                              ('01:02:26.43280', '-31:33:07.2237'),
                              ('01:36:08.50799', '-29:54:26.3540')

                              ])

draw_lines = get_reverse_map(
    [('alpha', 'iota'),
     ('iota', 'delta'),
     ('delta', 'gamma'),
     ('gamma', 'beta')
     ], star_names)

constellations(coordinates=sculptor_coordinates, star_names=star_names, constellation_name='',
               short_name='scl', line_coordinates=draw_lines, turn_half=True)
