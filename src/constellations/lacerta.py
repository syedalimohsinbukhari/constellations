"""Created on Sep 25 16:19:03 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta'}

lacerta_coordinates = array([('22:31:17.50131', '50:16:56.9682'), ('22:23:32.62400', '52:13:44.5600')])

draw_lines = [(0, 1)]

constellations(coordinates=lacerta_coordinates, star_names=star_names, constellation_name='Lacerta', short_name='lac',
               line_coordinates=draw_lines)
