"""Created on Nov 08 11:51:42 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta_\mathrm{A, B, C}', 2: 'gamma', 3: 'delta', 4: 'epsilon_\mathrm{A, B}', 5: 'zeta'}

monoceros_coordinates = array([('07:41:14.83300', '-09:33:04.0700'), ('06:28:49.07000', '-07:01:59.0250'),
                               ('06:14:51.33367', '-06:16:29.1880'), ('07:11:51.86000', '-00:29:33.9600'),
                               ('06:23:46.08471', '+04:35:34.3153'), ('08:08:35.64663', '-02:59:01.6361')])

draw_lines = [(0, 5), (5, 3), (3, 1), (1, 2), (3, 4)]

constellations(coordinates=monoceros_coordinates, star_names=star_names, constellation_name='Monoceros',
               short_name='mon', line_coordinates=draw_lines)
