"""Created on Sep 05 23:33:40 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha^1', 1: 'alpha^2', 2: 'beta'}

canes_venatici_coordinates = array([('12:56:01.66622', '38:19:06.1541'), ('12:56:00.43258', '38:18:53.3768'),
                                    ('12:33:44.54425', '41:21:26.9214')])

draw_lines = [(0, 2)]

constellations(coordinates=canes_venatici_coordinates, star_names=star_names, constellation_name='Canes Venatici',
               short_name='cvn', line_coordinates=draw_lines)
