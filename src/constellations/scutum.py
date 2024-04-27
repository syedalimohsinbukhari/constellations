"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']
#                                     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta'}

scutum_coordinates = array([('18:35:12.42776', '-8:14:38.6529'),
                            ('18:47:10.47250', '-4:44:52.3271'),
                            ('18:29:11.85388', '-14:33:56.9319'),
                            ('18:42:16.42705', '-9:03:09.2004'),
                            ('18:43:31.251', '-8:16:30.77'),
                            ('18:23:39.58309', '-8:56:03.7885'),
                            ('18:57:03.67027', '-5:50:46.7305')
                            ])

draw_lines = get_reverse_map(
    [('beta', 'alpha'),
     ('alpha', 'gamma'),
     ('gamma', 'delta'),
     ('delta', 'epsilon'),
     ('epsilon', 'beta')
     ], star_names)

constellations(coordinates=scutum_coordinates, star_names=star_names, constellation_name='scutum',
               short_name='sct', line_coordinates=draw_lines, turn_half=True)
