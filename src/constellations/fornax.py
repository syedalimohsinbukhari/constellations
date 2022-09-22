"""Created on Sep 23 02:05:40 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma^1', 3: 'gamma^2', 4: 'delta', 5: 'epsilon', 6: 'zeta', 7: 'iota^2',
              8: 'kappa', 9: 'lambda^1', 10: 'lambda^2', 11: 'mu', 12: 'nu', 13: 'pi', 14: 'phi', 15: 'omega'}

fornax_coordinates = array([('03:12:04.52770', '-28:59:15.4250'), ('02:49:05.41885', '-32:24:21.2319'),
                            ('02:49:50.96219', '-24:33:37.1290'), ('02:49:54.18220', '-27:56:31.1230'),
                            ('03:42:14.90238', '-31:56:18.0961'), ('03:01:37.62887', '-28:05:29.3737'),
                            ('02:59:36.18299', '-25:16:26.8853'), ('02:38:18.66153', '-30:11:38.6284'),
                            ('02:22:32.60343', '-23:48:00.4878'), ('02:33:07.02590', '-34:38:59.8820'),
                            ('02:36:58.60790', '-34:34:40.7140'), ('02:12:54.46962', '-30:43:25.7732'),
                            ('02:04:29.43861', '-29:17:48.5477'), ('02:01:14.72272', '-30:00:06.5913'),
                            ('02:28:01.70348', '-33:48:39.7382'), ('02:33:50.70081', '-28:13:56.3890')])

# delta and epsilon have same coordinates in WPedia

draw_lines = [(0, 1), (1, 12)]

constellations(coordinates=fornax_coordinates, star_names=star_names, constellation_name='Fornax', short_name='for',
               line_coordinates=draw_lines)
