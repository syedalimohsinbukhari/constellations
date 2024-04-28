"""Created on Sep 24 00:35:56 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta^1', 4: 'delta^2', 5: 'epsilon', 6: 'zeta', 7: 'eta',
              8: 'theta', 9: 'iota', 10: 'kappa', 11: 'lambda', 12: 'mu^1', 13: 'mu^2', 14: 'nu', 15: 'xi',
              16: 'o', 17: 'pi^1', 18: 'pi^2', 19: 'rho', 20: 'sigma^1', 21: 'sigma^2', 22: 'tau^1',
              23: 'tau^2', 24: 'tau^3', 25: 'upsilon', 26: 'phi'}

grus_coordinates = array([('22:08:13.98473', '-46:57:39.5078'), ('22:42:40.05027', '-46:53:04.4752'),
                          ('21:53:55.72620', '-37:21:53.4790'), ('22:29:16.17481', '-43:29:44.0245'),
                          ('22:29:45.43402', '-43:44:57.1968'), ('22:48:33.29833', '-51:19:00.7001'),
                          ('23:00:52.79777', '-52:45:14.8705'), ('22:45:37.88285', '-53:30:00.4405'),
                          ('23:06:52.73046', '-43:31:13.2857'), ('23:10:21.53755', '-45:14:48.1647'),
                          ('23:04:39.62786', '-53:57:53.6651'), ('22:06:06.88568', '-39:32:36.0659'),
                          ('22:15:36.93338', '-41:20:48.3558'), ('22:16:26.54790', '-41:37:37.8266'),
                          ('22:28:39.21034', '-39:07:54.4505'), ('21:32:05.87583', '-41:10:45.5242'),
                          ('23:26:36.57748', '-52:43:17.7656'), ('22:22:44.20571', '-45:56:52.6115'),
                          ('22:23:07.98704', '-45:55:42.5582'), ('22:43:29.97654', '-41:24:51.6467'),
                          ('22:39:29.30230', '-40:34:57.7391'), ('22:36:58.85405', '-40:35:27.7272'),
                          ('22:53:37.93200', '-48:35:53.8300'), ('22:55:16.14624', '-48:27:56.8622'),
                          ('22:56:47.80007', '-47:58:09.1992'), ('23:06:53.62552', '-38:53:32.2484'),
                          ('23:18:09.88466', '-40:49:27.7034')])

draw_lines = [(0, 1), (0, 3), (1, 3), (1, 5), (5, 6), (3, 12), (12, 11), (11, 2)]

constellations(coordinates=grus_coordinates, star_names=star_names, constellation_name='Grus', short_name='gru',
               line_coordinates=draw_lines)
