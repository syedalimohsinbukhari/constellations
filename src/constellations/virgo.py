"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
#      'o', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'o', 15: 'pi', 16: 'rho', 17: 'sigma',
              18: 'tau', 19: 'upsilon', 20: 'phi', 21: 'chi', 22: 'psi', 23: 'omega'}

virgo_coordinates = array([('13:25:11.579', '-11:09:40.75'),
                           ('11:50:41.71824', '+01:45:52.9910'),
                           ('12:41:39.64344', '-01:26:57.7421'),
                           ('12:55:36.20861', '+03:23:50.8932'),
                           ('13:02:10.59785', '+10:57:32.9415'),
                           ('13:34:41.591', '-00:35:44.95'),
                           ('12:19:54.35783', '-00:40:00.5095'),
                           ('13:09:56.99067', '-05:32:20.4185'),
                           ('14:16:00.86951', '-06:00:01.9633'),
                           ('14:12:53.74538', '-10:16:25.3340'),
                           ('14:19:06.59235', '-13:22:15.9459'),
                           ('14:43:03.62282', '-05:39:29.5327'),
                           ('11:45:51.55957', '+06:31:45.7413'),
                           ('11:45:17.04027', '+08:15:29.2150'),
                           ('12:05:12.54049', '+08:43:58.7498'),
                           ('12:00:52.39042', '+06:36:51.5571'),
                           ('12:41:53.05658', '+10:14:51.1699'),
                           ('13:17:36.28327', '+05:28:11.5221'),
                           ('14:01:38.79341', '+01:32:40.3145'),
                           ('14:19:32.47974', '-02:15:55.8587'),
                           ('14:28:12.13894', '-02:13:40.6579'),
                           ('12:39:14.76696', '-07:59:44.0338'),
                           ('12:54:21.16342', '-09:32:20.3783'),
                           ('11:38:27.60727', '+08:08:03.4663')
                           ])

draw_lines = get_reverse_map(
    [('tau', 'zeta'), ('zeta', 'iota'), ('iota', 'mu'), ('zeta', 'gamma'), ('gamma', 'theta'), ('theta', 'alpha'),
     ('gamma', 'delta'), ('delta', 'epsilon'), ('gamma', 'eta'), ('eta', 'beta'), ('beta', 'nu'), ('nu', 'o'),
     ('o', 'eta')
     ], star_names)

constellations(coordinates=virgo_coordinates, star_names=star_names, constellation_name='virgo',
               short_name='vir', line_coordinates=draw_lines, turn_half=True)
