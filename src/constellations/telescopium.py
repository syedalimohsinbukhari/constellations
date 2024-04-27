"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'delta^1', 'delta^2', 'epsilon', 'zeta', 'eta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'rho', 'tau']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'delta^1', 2: 'delta^2', 3: 'epsilon', 4: 'zeta', 5: 'eta', 6: 'iota', 7: 'kappa',
              8: 'lambda', 9: 'mu', 10: 'nu', 11: 'xi', 12: 'rho', 13: 'tau'}

telescopium_coordinates = array([('18:26:58.41604', '-45:58:06.4498'),
                                 ('18:31:45.43288', '-45:54:53.3166'),
                                 ('18:32:01.94437', '-45:45:26.5636'),
                                 ('18:11:13.7612', '-45:57:15.8824'),
                                 ('18:28:49.85980', '-49:04:14.1122'),
                                 ('19:22:51.20608', '-54:25:26.1456'),
                                 ('19:35:12.98634', '-48:05:57.1238'),
                                 ('18:52:39.64405', '-52:06:26.5372'),
                                 ('18:58:27.79251', '-52:56:19.1999'),
                                 ('19:30:34.6118', '-55:06:36.1901'),
                                 ('19:48:01.1977', '-56:21:45.3996'),
                                 ('20:07:23.15599', '-52:52:50.8490'),
                                 ('19:06:19.95580', '-52:20:27.2757'),
                                 ('18:29:55.9414', '-47:13:13.9500')

                                 ])

draw_lines = get_reverse_map(
    [('zeta', 'alpha'), ('alpha', 'epsilon')], star_names)

constellations(coordinates=telescopium_coordinates, star_names=star_names, constellation_name='telescopium',
               short_name='tel', line_coordinates=draw_lines, turn_half=True)
