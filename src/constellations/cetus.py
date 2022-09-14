"""Created on Sep 14 08:18:53 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa^1', 10: 'kappa^2', 11: 'lambda', 12: 'mu', 13: 'nu', 14: 'xi^1', 15: 'xi^2', 16: 'omicron',
              17: 'pi', 18: 'rho', 19: 'sigma', 20: 'tau', 21: 'upsilon', 22: 'phi^1', 23: 'phi^2', 24: 'phi^3',
              25: 'phi^4', 26: 'chi^1', 27: 'chi^2'}

cetus_coordinates = array([('03:02:16.77307', '04:05:23.0596'), ('00:43:35.37090', '-17:59:11.7827'),
                           ('02:43:18.03910', '03:14:08.9390'), ('02:39:28.95579', '+00:19:42.6345'),
                           ('02:39:33.82853', '-11:52:19.7132'), ('01:51:27.63482', '-10:20:06.1289'),
                           ('01:08:35.39148', '-10:10:56.1570'), ('01:24:01.40528', '-08:10:59.7212'),
                           ('00:19:25.67416', '-08:49:26.1111'), ('03:19:21.69600', '03:22:12.7120'),
                           ('03:21:06.80281', '03:04:32.23440'), ('02:59:42.89987', '08:54:26.4899'),
                           ('02:44:56.54098', '10:06:50.9089'), ('02:35:52.47300', '05:35:35.6900'),
                           ('02:12:59.99769', '08:50:48.2023'), ('02:28:09.55706', '08:27:36.2168'),
                           ('02:19:21.79210', '-02:58:39.4956'), ('02:44:07.36928', '-13:51:31.3130'),
                           ('02:25:57.00560', '-12:17:25.7104'), ('02:32:05.22884', '-15:14:40.8278'),
                           ('01:44:04.83380', '-15:56:14.9262'), ('02:00:00.30916', '-21:04:4.1946'),
                           ('00:44:11.40013', '-10:36:34.3816'), ('00:50:07.58859', '-10:38:39.5848'),
                           ('00:56:01.48867', '-11:15:59.4988'), ('00:58:43.86832', '-11:22:47.9147'),
                           ('01:49:35.10316', '-10:41:11.0674'), ('01:49:23.35579', '-10:42:12.8594')])

draw_lines = [(0, 2), (0, 11), (11, 12), (12, 15), (15, 13), (13, 2), (2, 3), (3, 16), (16, 5), (5, 7), (7, 6),
              (6, 8), (8, 1), (1, 20), (20, 5)]

constellations(coordinates=cetus_coordinates, star_names=star_names, constellation_name='Cetus', short_name='cet',
               line_coordinates=draw_lines, turn_half=True)