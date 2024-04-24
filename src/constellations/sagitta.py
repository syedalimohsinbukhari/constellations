"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha',
#                                      'beta',
#                                      'gamma',
#                                      'delta',
#                                      'epsilon',
#                                      'zeta',
#                                      'eta',
#                                      'theta'
#                                      ])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta'}

sagitta_coordinates = array([
    ('19:40:05.79185', '+18:00:50.0046'),
    ('19:41:02.93907', '+17:28:33.7528'),
    ('19:58:45.42863', '+19:29:31.7281'),
    ('19:47:23.26653', '+18:32:03.5203'),
    ('19:37:17.39324', '+16:27:46.0871'),
    ('19:48:58.65978', '+19:08:31.3516'),
    ('20:05:09.49303', '+19:59:27.8575'),
    ('20:09:56.64700', '+20:54:54.0940')

])

draw_lines = get_reverse_map(
    [('gamma','delta'),('delta','alpha'),('delta','beta')], star_names)

constellations(coordinates=sagitta_coordinates, star_names=star_names, constellation_name='sagitta',
               short_name='sge', line_coordinates=draw_lines, turn_half=True)
