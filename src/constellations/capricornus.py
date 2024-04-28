"""Created on Sep 07 20:21:04 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha^1', 1: 'alpha^2', 2: 'beta', 3: 'gamma', 4: 'delta', 5: 'epsilon', 6: 'zeta', 7: 'eta',
              8: 'theta', 9: 'iota', 10: 'kappa', 11: 'lambda', 12: 'mu', 13: 'nu', 14: 'xi^1', 15: 'xi^2',
              16: 'o^1', 17: 'o^2', 18: 'pi', 19: 'rho', 20: 'sigma', 21: 'tau^1', 22: 'tau^2',
              23: 'upsilon', 24: 'phi', 25: 'chi', 26: 'psi', 27: 'omega'}

capricornus_coordinates = array([('20:17:38.86910', '-12:30:29.5716'), ('20:18:03.25595', '-12:32:41.4684'),
                                 ('20:21:00.70000', '-14:46:53.0000'), ('21:40:05.45648', '-16:39:44.3072'),
                                 ('21:47:02.44424', '-16:07:38.2335'), ('21:37:04.83068', '-19:27:57.6464'),
                                 ('21:26:40.02634', '-22:24:40.8042'), ('21:04:24.30132', '-19:51:17.9711'),
                                 ('21:05:56.82783', '-17:13:58.3021'), ('21:22:14.79598', '-16:50:04.3580'),
                                 ('21:42:39.50710', '-18:51:58.7669'), ('21:46:32.09739', '-11:21:57.4391'),
                                 ('21:53:17.77054', '-13:33:06.3679'), ('20:20:39.81562', '-12:45:32.6844'),
                                 ('20:11:57.89778', '-12:23:32.6484'), ('20:12:25.87020', '-12:37:02.9967'),
                                 ('20:29:53.91117', '-18:34:59.4803'), ('20:29:52.59487', '-18:35:10.7447'),
                                 ('20:27:19.21088', '-18:12:42.1980'), ('20:28:51.61448', '-17:48:49.2693'),
                                 ('20:19:23.60402', '-19:07:06.6967'), ('20:37:21.20000', '-15:08:50.4000'),
                                 ('20:39:16.31779', '-14:57:17.1352'), ('20:40:02.94518', '-18:08:19.1664'),
                                 ('21:15:37.89982', '-20:39:06.1032'), ('21:08:33.62529', '-21:11:37.2177'),
                                 ('20:46:05.73263', '-25:16:15.2312'), ('20:51:49.29095', '-26:55:08.8912')])

draw_lines = [(0, 2), (0, 8), (8, 3), (3, 4), (2, 26), (26, 27), (4, 5), (5, 6), (6, 27)]

constellations(coordinates=capricornus_coordinates, star_names=star_names, constellation_name='Capricornus',
               short_name='cap', line_coordinates=draw_lines)
