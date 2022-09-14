"""Created on Sep 14 09:36:34 2022."""

from numpy import array

from src.constellations.utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta^1', 4: 'delta^2', 5: 'epsilon', 6: 'zeta', 7: 'eta',
              8: 'theta', 9: 'iota', 10: 'kappa', 11: 'mu^1', 12: 'mu^2', 13: 'nu', 14: 'pi'}

chamaeleon_coordinates = array([('08:18:31.55319', '-76:55:10.9964'), ('12:18:20.82459', '-79:18:44.0710'),
                                ('10:35:28.10720', '-78:36:28.0321'), ('10:45:16.31446', '-80:28:10.5409'),
                                ('10:45:47.00487', '-80:32:24.6785'), ('11:59:37.57634', '-78:13:18.6179'),
                                ('09:33:53.37609', '-80:56:28.5337'), ('08:41:19.51442', '-78:57:48.1023'),
                                ('08:20:38.54055', '-77:29:04.1173'), ('09:24:09.22580', '-80:47:12.7597'),
                                ('12:04:46.47090', '-76:31:08.6272'), ('10:00:43.79370', '-82:12:52.8125'),
                                ('10:04:07.14960', '-81:33:55.7280'), ('09:46:20.63010', '-76:46:34.0259'),
                                ('11:37:15.63631', '-75:53:47.5626')])

draw_lines = [(0, 8), (8, 2), (2, 5), (5, 1), (1, 3), (3, 2)]

constellations(coordinates=chamaeleon_coordinates, star_names=star_names, constellation_name='Chamaeleon',
               short_name='cha', line_coordinates=draw_lines)
