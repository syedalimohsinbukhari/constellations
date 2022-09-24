"""Created on Sep 24 02:47:25 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'zeta', 5: 'eta', 6: 'iota', 7: 'lambda', 8: 'mu',
              9: 'nu'}

horologium_coordinates = array([('04:14:00.11445', '-42:17:39.7232'), ('02:58:47.79642', '-64:04:16.6250'),
                                ('02:45:27.47800', '-63:42:16.3925'), ('04:10:50.58927', '-41:59:36.8537'),
                                ('02:40:39.61286', '-54:32:59.6836'), ('02:37:24.37297', '-52:32:35.0855'),
                                ('02:42:33.46650', '-50:48:01.0562'), ('02:24:53.91034', '-60:18:43.0170'),
                                ('03:03:36.81891', '-59:44:15.9925'), ('02:49:01.48700', '-62:48:23.4800')])

draw_lines = [(0, 6), (6, 5), (5, 4), (4, 8), (8, 1)]

constellations(coordinates=horologium_coordinates, star_names=star_names, constellation_name='Horologium',
               short_name='hor', line_coordinates=draw_lines)
