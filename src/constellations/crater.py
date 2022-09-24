"""Created on Sep 17 18:53:02 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'psi'}

crater_coordinates = array([('10:59:46.46486', '-18:17:55.6172'), ('11:11:39.48783', '-22:49:33.0593'),
                            ('11:24:52.92362', '-17:41:02.4300'), ('11:19:20.44756', '-14:46:42.7413'),
                            ('11:24:36.59017', '-10:51:33.5591'), ('11:44:45.77615', '-18:24:02.4298'),
                            ('11:56:00.95323', '-17:09:02.9781'), ('11:36:40.91335', '-09:48:08.0912'),
                            ('11:38:40.01668', '-13:12:06.9963'), ('11:27:09.51622', '-12:21:24.2934'),
                            ('11:23:21.88432', '-18:46:47.8910'), ('11:12:30.37188', '-18:29:59.4995')])

draw_lines = [(0, 1), (0, 3), (3, 4), (4, 7), (1, 2), (2, 3), (2, 5), (5, 6)]

constellations(coordinates=crater_coordinates, star_names=star_names, constellation_name='Crater', short_name='crt',
               line_coordinates=draw_lines)
