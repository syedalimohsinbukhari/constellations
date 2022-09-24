"""Created on Sep 22 20:45:46 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma^1', 3: 'gamma^2', 4: 'delta', 5: 'epsilon', 6: 'zeta', 7: 'eta',
              8: 'theta', 9: 'iota', 10: 'kappa', 11: 'rho^{AQL}'}

delphinus_coordinates = array([('20:39:38.28720', '15:54:43.4637'), ('20:37:32.94130', '14:35:42.3195'),
                               ('20:46:38.86045', '16:07:26.8516'), ('20:46:39.00000', '16:07:27.4358'),
                               ('20:43:27.53338', '15:04:28.4773'), ('20:33:12.77192', '11:18:11.7412'),
                               ('20:35:18.53563', '14:40:27.1675'), ('20:33:57.04099', '13:01:38.1437'),
                               ('20:38:43.98644', '13:18:54.4543'), ('20:37:49.11980', '11:22:39.6308'),
                               ('20:39:07.78430', '10:05:10.3383'), ('20:14:16.61886', '15:11:51.3923')])

draw_lines = [(0, 2), (2, 4), (4, 1), (1, 0), (1, 5)]

constellations(coordinates=delphinus_coordinates, star_names=star_names, constellation_name='Delphinus',
               short_name='del', line_coordinates=draw_lines)
