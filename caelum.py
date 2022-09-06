"""Created on Sep 05 14:11:06 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma^1', 3: 'delta', 4: 'zeta', 5: 'lambda', 6: 'nu'}

caelum_coordinates = array([('04:40:33.71250', '-41:51:49.5090'), ('04:42:03.48029', '-37:08:39.4641'),
                            ('05:04:24.40000', '-35:28:58.6900'), ('04:30:50.09903', '-44:57:13.5035'),
                            ('04:47:49.57719', '-30:01:13.3391'), ('04:43:44.27211', '-41:03:53.2340'),
                            ('04:50:16.18032', '-41:19:15.0557')])

draw_lines = [(3, 0), (0, 1), (1, 2)]

constellations(coordinates=caelum_coordinates, star_names=star_names, constellation_name='Caelum', short_name='cae',
               line_coordinates=draw_lines)
