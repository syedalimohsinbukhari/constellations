"""Created on Sep 17 19:02:05 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta^1',
              8: 'theta^2', 9: 'iota', 10: 'kappa', 11: 'lambda', 12: 'mu^1', 13: 'mu^2'}

crux_coordinates = array([('12:26:35.89522', '-63:05:56.7343'), ('12:47:43.26877', '-59:41:19.5792'),
                          ('12:31:09.96000', '-57:06:47.5680'), ('12:15:08.71673', '-58:44:56.1369'),
                          ('12:21:21.60936', '-60:24:04.1291'), ('12:18:26.24772', '-64:00:11.0528'),
                          ('12:06:52.89900', '-64:36:49.4244'), ('12:03:01.50130', '-63:18:46.5406'),
                          ('12:04:19.21504', '-63:09:56.5537'), ('12:45:38.05019', '-60:58:52.7536'),
                          ('12:53:48.91920', '-60:22:34.4808'), ('12:54:39.18258', '-59:08:48.1229'),
                          ('12:54:35.62490', '-57:10:40.5270'), ('12:54:36.88650', '-57:10:07.2140')])

draw_lines = [(0, 2), (1, 3)]

constellations(coordinates=crux_coordinates, star_names=star_names, constellation_name='Crux', short_name='cru',
               line_coordinates=draw_lines)
