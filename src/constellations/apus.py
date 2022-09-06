"""Created on Sep 03 04:02:05 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa^1', 10: 'kappa^2'}

apus_coordinates = array([('14:47:51.71203', '-79:02:41.1032'), ('16:43:04.65651', '-77:31:02.7629'),
                          ('16:33:27.08379', '-78:53:49.7372'), ('16:20:20.80462', '-78:41:44.6889'),
                          ('14:22:23.16467', '-80:06:32.2053'), ('17:21:59.47633', '-67:46:14.4072'),
                          ('14:18:13.89774', '-81:00:27.9300'), ('14:05:19.87784', '-76:47:48.3204'),
                          ('17:22:05.87559', '-70:07:23.5400'), ('15:31:30.82213', '-73:23:22.5295'),
                          ('15:40:21.33360', '-73:26:48.0648')])

draw_lines = [(0, 3), (3, 1), (1, 2)]

constellations(coordinates=apus_coordinates, star_names=star_names, constellation_name='apus', short_name='aps',
               line_coordinates=draw_lines)
