"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta',
#                                      'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'o', 'pi',
#                                      'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi^1', 'psi^2', 'psi^3',
#                                      'omega'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'o', 15: 'pi', 16: 'rho', 17: 'sigma',
              18: 'tau', 19: 'upsilon', 20: 'phi', 21: 'chi', 22: 'psi^1', 23: 'psi^2', 24: 'psi^3', 25: 'omega'}

pisces_coordinates = array([('02:02:02.81972', '+02:45:49.5410'),
                            ('23:03:52.61349', '+03:49:12.1662'),
                            ('23:17:09.937', '+03:16:56.25'),
                            ('00:48:40.94433', '+07:35:06.2926'),
                            ('01:02:56.60862', '+07:53:24.4855'),
                            ('01:13:45.17477', '+07:34:31.2745'),
                            ('01:31:29.01026', '+15:20:44.9685'),
                            ('23:27:58.09529', '+06:22:44.3720'),
                            ('23:39:57.04138', '+05:37:34.6475'),
                            ('23:26:55.95586', '+01:15:20.1900'),
                            ('23:42:02.80612', '+01:46:48.1484'),
                            ('01:30:11.11444', '+06:08:37.7577'),
                            ('01:41:25.89391', '+05:29:15.4062'),
                            ('01:45:23.63185', '+09:09:27.8530'),
                            ('01:45:23.63185', '+09:09:27.8530'),
                            ('01:37:05.91523', '+12:08:29.5186'),
                            ('01:26:15.26209', '+19:10:20.4526'),
                            ('01:02:49.09645', '+31:48:15.3471'),
                            ('01:11:39.63647', '+30:05:22.6909'),
                            ('01:19:27.99289', '+27:15:50.6155'),
                            ('01:13:44.94617', '+24:35:01.3249'),
                            ('01:11:27.21877', '+21:02:04.7406'),
                            ('01:05:40.95527', '+21:28:23.4489'),
                            ('01:07:57.16387', '+20:44:20.8310'),
                            ('01:09:49.20099', '+19:39:30.2694'),
                            ('23:59:18.69064', '+06:51:47.9562')
                            ])

draw_lines = get_reverse_map(
    [('tau', 'phi'), ('phi', 'rho'), ('rho', 'eta'), ('eta', 'o'), ('o', 'alpha'), ('tau', 'upsilon'),
     ('upsilon', 'phi'), ('alpha', 'nu'), ('nu', 'mu'), ('mu', 'zeta'), ('zeta', 'epsilon'),
     ('epsilon', 'delta'), ('delta', 'omega'), ('omega', 'iota'), ('iota', 'theta'), ('theta', 'gamma'),
     ('gamma', 'kappa'),
     ('kappa', 'lambda'), ('lambda', 'iota')], star_names)

constellations(coordinates=pisces_coordinates, star_names=star_names, constellation_name='pisces',
               short_name='psc', line_coordinates=draw_lines,turn_half=True )
