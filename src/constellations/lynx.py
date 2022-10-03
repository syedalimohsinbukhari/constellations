"""Created on Oct 03 16:08:58 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'psi^{10}_{AUR}'}

lynx_coordinates = array([('09:21:03.30074', '34:23:33.2245'), ('06:57:37.10709', '45:05:38.7404')])

draw_lines = [(0, 0)]

constellations(coordinates=lynx_coordinates, star_names=star_names, constellation_name='Lynx', short_name='lyn',
               line_coordinates=draw_lines)
