"""Created on Sep 16 22:47:46 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma'}

coma_berenices_coordinates = array([('13:09:59.28500', '17:31:46.0400'), ('13:11:52.39379', '27:52:41.4535'),
                                    ('12:26:56.27207', '28:16:06.3211')])

draw_lines = [(0, 1), (1, 2)]

constellations(coordinates=coma_berenices_coordinates, star_names=star_names, constellation_name='Coma Berenices',
               short_name='com', line_coordinates=draw_lines)
