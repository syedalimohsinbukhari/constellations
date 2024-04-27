"""Created on Sep 22 21:10:38 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha^1', 1: 'alpha^2', 2: 'beta', 3: 'gamma', 4: 'delta', 5: 'epsilon', 6: 'zeta^1', 7: 'zeta^2',
              8: 'eta^1', 9: 'eta^2', 10: 'theta', 11: 'lambda', 12: 'nu'}

dorado_coordinates = array([('04:33:59.77800', '-55:02:41.9100'), ('04:33:59.78200', '-55:02:42.3900'),
                            ('05:33:37.51253', '-62:29:23.3231'), ('04:16:01.58823', '-51:29:11.9191'),
                            ('05:44:46.37811', '-65:44:07.9011'), ('05:49:53.52107', '-66:54:04.2787'),
                            ('05:05:30.65618', '-57:28:21.7289'), ('05:05:47.37235', '-57:33:13.7974'),
                            ('06:06:09.38154', '-66:02:22.6304'), ('06:11:15.00000', '-65:35:21.9000'),
                            ('05:13:45.45627', '-67:11:06.9351'), ('05:26:19.26577', '-58:54:45.06402'),
                            ('06:08:44.26199', '-68:50:36.2797')])

draw_lines = [(3, 0), (0, 6), (6, 2), (0, 2), (2, 4)]

constellations(coordinates=dorado_coordinates, star_names=star_names, constellation_name='Dorado', short_name='dor',
               line_coordinates=draw_lines)
