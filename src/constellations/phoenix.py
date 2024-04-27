"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta',
#                                      'iota', 'kappa', 'lambda^1', 'lambda^2', 'mu', 'nu', 'xi', 'pi',
#                                      'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda^1', 11: 'lambda^2', 12: 'mu', 13: 'nu', 14: 'xi', 15: 'pi', 16: 'rho',
              17: 'sigma', 18: 'tau', 19: 'upsilon', 20: 'phi', 21: 'chi', 22: 'psi', 23: 'omega'}

phoenix_coordinates = array([('00:26:17.06309', '-42:18:21.7712'),
                             ('01:06:05.03952', '-46:43:06.2785'),
                             ('01:28:21.92727', '-43:19:05.6502'),
                             ('01:31:15.10475', '-49:04:21.7308'),
                             ('00:09:24.64154', '-45:44:50.7315'),
                             ('01:08:23.080', '-55:14:44.700'),
                             ('00:43:21.23841', '-57:27:47.0073'),
                             ('23:39:27.92', '-46:38:16.4'),
                             ('23:35:04.57082', '-42:36:54.5409'),
                             ('00:26:12.20183', '-43:40:47.3929'),
                             ('00:31:24.98200', '-48:48:12.6759'),
                             ('00:35:41.13', '-48:00:02.4'),
                             ('00:41:19.55229', '-46:05:06.0184'),
                             ('01:15:11.12150', '-45:31:53.9954'),
                             ('00:41:46.30191', '-56:30:05.2370'),
                             ('23:58:55.72', '-52:44:45.4'),
                             ('00:50:41.186', '-50:59:12.54'),
                             ('23:47:15.99', '-50:13:35.1'),
                             ('00:01:04.60', '-48:48:35.5'),
                             ('01:07:47.83', '-41:29:13.0'),
                             ('01:54:22.032', '-42:29:48.94'),
                             ('01:53:38.74103', '-46:18:09.6048'),
                             ('01:02:01.81', '-57:00:08.7')
                             ])

draw_lines = get_reverse_map(
    [('gamma', 'nu'), ('nu', 'beta'), ('beta', 'zeta'), ('zeta', 'delta'), ('delta', 'gamma'), ('beta', 'alpha'),
     ('alpha', 'epsilon'), ('epsilon', 'beta')], star_names)

constellations(coordinates=phoenix_coordinates, star_names=star_names, constellation_name='phoenix',
               short_name='phe', line_coordinates=draw_lines,turn_half=True )
