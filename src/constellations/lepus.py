"""Created on Sep 25 22:42:54 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu'}

lepus_coordinates = array([('05:32:43.81612', '-17:49:20.2414'), ('05:28:14.72316', '-20:45:33.9878'),
                           ('05:44:27.79089', '-22:26:54.1808'), ('05:51:19.29613', '-20:52:44.7232'),
                           ('05:05:27.66537', '-22:22:15.7239'), ('05:46:57.34096', '-14:49:19.0199'),
                           ('05:56:24.29300', '-14:10:03.7189'), ('06:06:09.32339', '-14:56:06.9188'),
                           ('05:12:17.90190', '-11:52:09.1863'), ('05:13:13.87761', '-12:56:28.6463'),
                           ('05:19:34.52405', '-13:10:36.4408'), ('05:12:55.90296', '-16:12:19.6686'),
                           ('05:19:59.02275', '-12:18:56.1139')])

draw_lines = [(0, 1), (0, 5), (5, 6), (6, 7), (7, 3), (3, 2), (2, 1), (1, 4), (4, 11), (11, 0), (11, 9), (11, 10)]

constellations(coordinates=lepus_coordinates, star_names=star_names, constellation_name='Lepus', short_name='lep',
               line_coordinates=draw_lines)
