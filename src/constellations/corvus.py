"""Created on Sep 17 18:46:27 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta'}

corvus_coordinates = array([('12:08:24.81652', '-24:43:43.9504'), ('12:34:23.23484', '-23:23:48.3374'),
                            ('12:15:48.37081', '-17:32:30.9496'), ('12:29:51.85517', '-16:30:55.5525'),
                            ('12:10:07.48058', '-22:37:11.1620'), ('12:20:33.64200', '-22:12:57.2410'),
                            ('12:32:04.22653', '-16:11:45.6165')])

draw_lines = [(0, 4), (4, 1), (4, 2), (2, 3), (3, 6), (3, 1)]

constellations(coordinates=corvus_coordinates, star_names=star_names, constellation_name='Corvus', short_name='crv',
               line_coordinates=draw_lines)
