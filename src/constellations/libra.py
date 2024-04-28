"""Created on Sep 28 19:07:06 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha^1', 1: 'alpha^2', 2: 'beta', 3: 'gamma', 4: 'delta', 5: 'eta', 6: 'zeta^1',
              7: 'zeta^3', 8: 'zeta^4', 9: 'eta', 10: 'theta', 11: 'iota^1', 12: 'iota^2', 13: 'kappa', 14: 'lambda',
              15: 'mu', 16: 'nu', 17: 'xi^1', 18: 'xi^2', 19: 'o', 20: 'sigma', 21: 'tau', 22: 'upsilon'}

libra_coordinates = array([('14:50:41.18097', '-15:59:50.0482'), ('14:50:52.71309', '-16:02:30.3955'),
                           ('15:17:00.41382', '-09:22:58.4919'), ('15:35:31.57881', '-14:47:22.3278'),
                           ('15:00:58.34830', '-08:31:08.2104'), ('15:24:11.87101', '-10:19:20.1740'),
                           ('15:25:15.40819', '-16:42:59.3475'), ('15:30:40.40132', '-16:36:34.0647'),
                           ('15:32:55.22125', '-16:51:10.2412'), ('15:44:04.39946', '-15:40:22.2033'),
                           ('15:53:49.53806', '-16:43:45.4582'), ('15:12:13.29025', '-19:47:30.1592'),
                           ('15:13:19.19346', '-19:38:51.2738'), ('15:41:56.79858', '-19:40:43.7745'),
                           ('15:53:20.05463', '-20:10:01.4177'), ('14:49:19.05130', '-14:08:56.4766'),
                           ('15:06:37.59651', '-16:15:24.5469'), ('14:54:22.87411', '-11:53:54.0613'),
                           ('14:56:46.11504', '-11:24:34.9201'), ('15:21:01.38935', '-15:32:54.0655'),
                           ('15:04:04.21608', '-25:16:55.0606'), ('15:38:39.36950', '-29:46:39.8956'),
                           ('15:37:01.45020', '-28:08:06.2926')])

draw_lines = [(0, 2), (0, 3), (0, 20), (2, 3), (3, 22), (22, 21)]

constellations(coordinates=libra_coordinates, star_names=star_names, constellation_name='Libra', short_name='lib',
               line_coordinates=draw_lines)
