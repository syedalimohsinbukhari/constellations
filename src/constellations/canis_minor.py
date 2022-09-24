"""Created on Sep 07 19:35:52 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta^1', 4: 'delta^2', 5: 'delta^3', 6: 'epsilon', 7: 'zeta',
              8: 'eta'}

canis_minor_coordinates = array([('07:39:18.11950', '05:13:29.9552'), ('07:27:09.04174', '08:17:21.5368'),
                                 ('07:28:09.79333', '08:55:31.9068'), ('07:32:05.94912', '01:54:52.1263'),
                                 ('07:33:11.66576', '03:17:25.3551'), ('07:34:15.89238', '03:22:18.1956'),
                                 ('07:25:38.89613', '09:16:33.9541'), ('07:51:41.98835', '01:46:00.7395'),
                                 ('07:28:02.07527', '06:56:31.0897')])

draw_lines = [(0, 1)]

constellations(coordinates=canis_minor_coordinates, star_names=star_names, constellation_name='Canis Minor',
               short_name='cmi', line_coordinates=draw_lines)
