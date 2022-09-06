"""Created on Sep 05 14:23:49 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma'}

camelopardalis_coordinates = array([('04:54:03.01040', '66:20:33.6365'), ('05:03:25.08963', '60:26:32.0895'),
                                    ('03:50:21.50892', '71:19:56.1480')])

draw_lines = [(0, 1)]

constellations(coordinates=camelopardalis_coordinates, star_names=star_names, constellation_name='Camelopardalis',
               short_name='cam', line_coordinates=draw_lines)
