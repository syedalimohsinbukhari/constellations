"""Created on Sep 07 23:21:07 2022."""

from numpy import array

from src.constellations.utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'epsilon', 3: 'eta', 4: 'theta', 5: 'iota', 6: 'upsilon', 7: 'chi', 8: 'omega'}

carina_coordinates = array([('06:23:57.10988', '-52:41:44.3810'), ('09:13:11.97746', '-69:43:01.9473'),
                            ('08:22:30.83526', '-59:30:34.1431'), ('10:45:03.59100', '-59:41:04.2600'),
                            ('10:42:57.40197', '-64:23:40.0208'), ('09:17:05.40686', '-59:16:30.8353'),
                            ('09:47:06.12170', '-65:04:19.2267'), ('07:56:46.69000', '-52:58:55.9500'),
                            ('10:13:44.21739', '-70:02:16.4563')])

draw_lines = [(0, 2), (2, 5), (5, 6), (6, 1), (1, 8), (8, 4), (4, 3), (3, 5)]

constellations(coordinates=carina_coordinates, star_names=star_names, constellation_name='Carina', short_name='car',
               line_coordinates=draw_lines)
