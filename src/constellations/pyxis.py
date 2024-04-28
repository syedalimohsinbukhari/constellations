"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from utilities.Constellations import constellations
from utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'kappa',
              9: 'lambda'}

pyxis_coordinates = array([('08:43:35.53756', '-33:11:10.9898'), ('08:40:06.14363', '-35:18:30.0000'),
                           ('08:50:31.92282', '-27:42:35.4421'), ('08:55:31.56948', '-27:40:54.7315'),
                           ('09:09:56.41024', '-30:21:55.4460'), ('08:39:42.47410', '-29:33:39.8989'),
                           ('08:37:52.15248', '-26:15:18.0063'), ('09:21:29.60000', '-25:57:55.5000'),
                           ('09:08:02.88015', '-25:51:30.7331'), ('09:23:12.25099', '-28:50:01.9420')])

draw_lines = get_reverse_map([('gamma', 'alpha'), ('alpha', 'beta')], star_names)

constellations(coordinates=pyxis_coordinates, star_names=star_names, constellation_name='pyxis',
               short_name='pyx', line_coordinates=draw_lines, turn_half=True)
