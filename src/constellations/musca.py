"""Created on Nov 08 11:58:41 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta^1', 6: 'zeta^2', 7: 'eta',
              8: 'theta', 9: 'iota^1', 10: 'iota^2', 11: 'lambda', 12: 'mu', 13: 'lambda_{Cha}'}

musca_coordinates = array([('12:37:11.01789', '-69:08:08.0332'), ('12:46:16.80410', '-68:06:29.2164'),
                           ('12:32:28.01343', '-72:07:58.7597'), ('13:02:16.26474', '-71:32:55.8752'),
                           ('12:17:34.27716', '-67:57:38.6486'), ('12:22:12.04737', '-68:18:26.3733'),
                           ('12:22:07.34002', '-67:31:19.5871'), ('13:15:14.94123', '-67:53:40.5276'),
                           ('13:08:07.15286', '-65:18:21.6819'), ('13:25:07.11942', '-74:53:16.1512'),
                           ('13:27:18.49881', '-74:41:30.3200'), ('11:45:36.41916', '-66:43:43.5440'),
                           ('11:48:14.53282', '-66:48:53.6712'), ('12:07:49.87515', '-75:22:01.2583')])

draw_lines = [(0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (4, 11)]

constellations(coordinates=musca_coordinates, star_names=star_names, constellation_name='Musca', short_name='mus',
               line_coordinates=draw_lines)
