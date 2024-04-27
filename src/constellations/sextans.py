"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon'}

sextans_coordinates = array([('10:07:56.29556', '-00:22:17.8621'), ('10:30:17.48000', '-00:38:13.3000'),
                             ('09:52:30.43727', '-08:06:18.1269'), ('10:29:28.70222', '-02:44:20.6862'),
                             ('10:17:37.80200', '-08:04:08.0898')])

draw_lines = get_reverse_map([('delta', 'beta'), ('beta', 'alpha'), ('alpha', 'gamma')], star_names)

constellations(coordinates=sextans_coordinates, star_names=star_names, constellation_name='sextans',
               short_name='sex', line_coordinates=draw_lines, turn_half=True)
