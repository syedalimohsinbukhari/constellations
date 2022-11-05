"""Created on Nov 05 15:52:59 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta^1',
              8: 'theta^2', 9: 'iota', 10: 'nu'}

microscopium_coordinates = array([('20:49:58.08100', '-33:46:46.9344'), ('20:51:58.76180', '-33:10:40.7051'),
                                  ('21:01:17.46047', '-32:15:27.9574'), ('21:06:01.14597', '-30:07:30.4290'),
                                  ('21:17:56.28399', '-32:10:21.1515'), ('21:02:57.95290', '-38:37:53.2099'),
                                  ('21:06:25.51950', '-41:23:09.4805'), ('21:20:45.62633', '-40:48:34.3607'),
                                  ('21:24:24.81796', '-41:00:24.1033'), ('20:48:29.14779', '-43:59:18.6369')])

draw_lines = [(0, 9), (9, 7), (7, 4), (4, 2), (2, 0)]

constellations(coordinates=microscopium_coordinates, star_names=star_names, constellation_name='Microscopium',
               short_name='mic', line_coordinates=draw_lines)
