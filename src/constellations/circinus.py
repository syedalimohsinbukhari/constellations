"""Created on Sep 14 09:54:45 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta'}

circinus_coordinates = array([('14:42:30.41958', '-64:58:30.4934'), ('15:17:30.84880', '-58:48:04.3384'),
                              ('15:23:22.64294', '-59:19:14.8131'), ('15:16:56.89610', '-60:57:26.1072'),
                              ('15:17:38.88983', '-63:36:37.6734'), ('14:54:42.58159', '-65:59:27.9460'),
                              ('15:04:48.18600', '-64:01:52.8611'), ('14:56:43.98700', '-62:46:51.6600')])

draw_lines = [(0, 1), (0, 2)]

constellations(coordinates=circinus_coordinates, star_names=star_names, constellation_name='Circinus', short_name='cir',
               line_coordinates=draw_lines)
