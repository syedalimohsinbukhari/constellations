"""Created on Sep 03 05:47:26 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'omicron', 15: 'pi', 16: 'sigma', 17: 'tau',
              18: 'upsilon', 19: 'phi', 20: 'chi', 21: 'psi', 22: 'omega^1', 23: 'omega^2'}

aquila_coordinates = array([('19:50:46.99855', '08:52:05.9563'), ('19:55:18.79256', '06:24:24.3425'),
                            ('19:46:15.58029', '10:36:47.7408'), ('19:25:29.90139', '03:06:53.2061'),
                            ('18:59:37.36161', '15:04:05.8807'), ('19:05:24.60802', '13:51:48.5182'),
                            ('19:52:28.36775', '01:00:20.3696'), ('20:11:18.28528', '-0:49:17.2626'),
                            ('19:36:43.27606', '-1:17:11.7611'), ('19:36:53.44952', '-7:01:38.9176'),
                            ('19:06:14.93898', '-4:52:57.2007'), ('19:34:05.35290', '07:22:44.1890'),
                            ('19:26:31.08926', '00:20:18.8549'), ('19:54:14.88184', '08:27:41.2299'),
                            ('19:51:01.64400', '10:24:56.5992'), ('19:48:42.05765', '11:48:57.2177'),
                            ('19:39:11.64246', '05:23:51.9797'), ('20:04:08.31506', '07:16:40.6705'),
                            ('19:45:39.94732', '07:36:47.3626'), ('19:56:14.25183', '11:25:25.3931'),
                            ('19:42:34.00828', '11:49:35.7023'), ('19:44:34.19086', '13:18:10.0063'),
                            ('19:17:48.99957', '11:35:43.5234'), ('19:19:53.06713', '11:32:05.8722')])

draw_lines = [(0, 1), (0, 2), (0, 5), (0, 3), (5, 3), (3, 6), (6, 7), (7, 1), (3, 10)]

constellations(coordinates=aquila_coordinates, star_names=star_names, constellation_name='Aquila', short_name='aql',
               line_coordinates=draw_lines)
