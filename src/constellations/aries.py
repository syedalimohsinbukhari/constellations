"""Created on Sep 03 20:00:36 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'omicron', 15: 'pi', 16: 'rho^1', 17: 'rho^2',
              18: 'rho^3', 19: 'sigma', 20: 'tau^1', 21: 'tau^2'}

aries_coordinates = array([('02:07:10.40570', '23:27:44.7032'), ('01:54:38.41099', '20:48:28.9133'),
                           ('01:53:31.81479', '19:17:37.8790'), ('03:11:37.76465', '19:43:36.0397'),
                           ('02:59:12.72536', '21:20:25.5575'), ('03:41:54.09143', '21:02:39.9952'),
                           ('02:12:48.08568', '21:12:39.5776'), ('02:18:07.53022', '19:54:04.1717'),
                           ('01:57:21.05476', '17:49:03.1202'), ('02:06:33.92497', '22:38:53.9476'),
                           ('01:57:55.71647', '23:35:45.8295'), ('02:42:21.93980', '20:00:41.2612'),
                           ('02:38:48.99425', '21:57:41.0616'), ('02:24:49.05655', '10:36:38.0236'),
                           ('02:44:32.97317', '15:18:42.7085'), ('02:49:17.55924', '17:27:51.5168'),
                           ('02:54:55.19994', '17:44:05.1102'), ('02:55:48.49800', '18:19:53.9029'),
                           ('02:56:25.15490', '18:01:23.2277'), ('02:51:29.58618', '15:04:55.4438'),
                           ('03:21:13.62462', '21:08:49.4390'), ('03:22:45.24006', '20:44:31.4382')])

draw_lines = [(0, 1), (1, 2)]

constellations(coordinates=aries_coordinates, star_names=star_names, constellation_name='Aries', short_name='ari',
               line_coordinates=draw_lines)