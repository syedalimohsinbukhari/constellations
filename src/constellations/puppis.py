"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from utilities.Constellations import constellations
from utilities.others_ import get_reverse_map

star_names = {0: 'zeta', 1: 'nu', 2: 'xi', 3: 'o', 4: 'pi', 5: 'rho', 6: 'sigma', 7: 'tau', 8: 'upsilon^1',
              9: 'upsilon^2', 10: 'chi', 11: 'l_2'}

puppis_coordinates = array([('08:03:35.10000', '-40:00:11.6000'), ('06:37:45.67135', '-43:11:45.3602'),
                            ('07:49:17.65567', '-24:51:35.2305'), ('07:48:05.16839', '-25:56:13.8123'),
                            ('07:17:08.55678', '-37:05:50.8962'), ('08:07:32.64882', '-24:18:15.5679'),
                            ('07:29:13.83049', '-43:18:05.1597'), ('06:49:56.16846', '-50:36:52.4437'),
                            ('07:18:18.39335', '-36:44:02.2329'), ('07:18:38.18632', '-36:44:33.8557'),
                            ('07:57:40.10678', '-30:20:04.4491'), ('07:13:32.31810', '-44:38:23.0630')])

draw_lines = get_reverse_map([('rho', 'xi'), ('xi', 'o'), ('xi', 'pi'), ('pi', 'nu'), ('zeta', 'rho')], star_names)

constellations(coordinates=puppis_coordinates, star_names=star_names, constellation_name='puppis',
               short_name='pup', line_coordinates=draw_lines, turn_half=True)
