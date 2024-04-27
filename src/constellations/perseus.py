"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'omicron', 15: 'pi', 16: 'rho', 17: 'sigma',
              18: 'tau', 19: 'phi', 20: 'psi', 21: 'omega', 22: 'b'}

perseus_coordinates = array([('03:24:19.37009', '49:51:40.24550'), ('03:08:10.13245', '40:57:20.32800'),
                             ('03:04:47.79074', '53:30:23.16870'), ('03:42:55.50426', '47:47:15.17460'),
                             ('03:57:51.23205', '40:00:36.77520'), ('03:54:07.92248', '31:53:01.08120'),
                             ('02:50:41.76600', '55:53:43.78760'), ('02:44:11.98704', '49:13:42.41110'),
                             ('03:09:04.02000', '49:36:47.80000'), ('03:09:29.77156', '44:51:27.14630'),
                             ('04:06:35.04360', '50:21:04.55000'), ('04:14:53.86253', '48:24:33.59120'),
                             ('03:45:11.63204', '42:34:42.78290'), ('03:58:57.90229', '35:47:27.71320'),
                             ('03:44:19.13377', '32:17:17.68740'), ('02:58:45.66858', '39:39:45.82120'),
                             ('03:05:10.59385', '38:50:24.99430'), ('03:30:34.48545', '47:59:42.78080'),
                             ('02:45:15.46108', '52:45:44.92400'), ('01:43:39.63792', '50:41:19.43280'),
                             ('03:36:29.37982', '48:11:33.47890'), ('03:11:17.38161', '39:36:41.70140'),
                             ('04:18:14.61690', '50:17:43.80580')])

draw_lines = get_reverse_map([('alpha', 'gamma'), ('alpha', 'iota'), ('iota', 'theta'), ('theta', 'phi'),
                              ('alpha', 'delta'), ('gamma', 'eta'), ('gamma', 'tau'), ('eta', 'tau'), ('tau', 'iota'),
                              ('delta', 'mu'), ('mu', 'lambda'), ('delta', 'epsilon'), ('epsilon', 'beta'),
                              ('epsilon', 'xi'), ('xi', 'zeta'), ('zeta', 'omicron'), ('beta', 'rho'),
                              ('beta', 'kappa'), ('kappa', 'iota')], star_names)

constellations(coordinates=perseus_coordinates, star_names=star_names, constellation_name='perseus',
               short_name='per', line_coordinates=draw_lines)
