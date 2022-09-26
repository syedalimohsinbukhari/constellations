"""Created on Sep 25 22:40:22 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'beta'}

leo_minor_coordinates = array([('10:27:53.00000', '36:42:25.9600')])

draw_lines = [(0, 0)]

constellations(coordinates=leo_minor_coordinates, star_names=star_names, constellation_name='Leo Minor',
               short_name='lmi', line_coordinates=draw_lines)
