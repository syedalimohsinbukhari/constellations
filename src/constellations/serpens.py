"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
#      'omicron', 'pi', 'rho', 'sigma', 'tau^1', 'tau^2', 'tau^3', 'tau^4', 'tau^5', 'tau^6', 'tau^7', 'tau^8', 'upsilon',
#      'phi', 'chi', 'psi', 'omega'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'omicron', 15: 'pi', 16: 'rho', 17: 'sigma',
              18: 'tau^1', 19: 'tau^2', 20: 'tau^3', 21: 'tau^4', 22: 'tau^5', 23: 'tau^6', 24: 'tau^7', 25: 'tau^8',
              26: 'upsilon', 27: 'phi', 28: 'chi', 29: 'psi', 30: 'omega'}

serpens_coordinates = array([('15:44:16.07431', '+06:25:32.2633'),
                             ('15:46:11.25435', '+15:25:18.5959'),
                             ('15:56:27.18269', '+15:39:41.8206'),
                             ('15:34:48.14762', '+10:32:19.9248'),
                             ('15:50:48.96622', '+04:28:39.8311'),
                             ('18:00:29.0', '-03:41:25'),
                             ('18:21:18.60056', '-02:53:55.7766'),
                             ('18:56:13.18', '+04:12:12.9'),
                             ('15:41:33.05469', '+19:40:13.4380'),
                             ('15:48:44.37676', '+18:08:29.6342'),
                             ('15:46:26.61423', '+07:21:11.0475'),
                             ('15:49:37.20696', '-03:25:48.7358'),
                             ('17:20:49.66149', '-12:50:48.7533'),
                             ('17:37:35.19983', '-15:23:54.7940'),
                             ('17:41:24.87286', '-12:52:31.1086'),
                             ('16:02:17.69166', '+22:48:16.0302'),
                             ('15:51:15.90985', '+20:58:40.5166'),
                             ('16:22:04.34753', '+01:01:44.5534'),
                             ('15:25:47.39664', '+15:25:40.9307'),
                             ('15:32:09.67495', '+16:03:22.2056'),
                             ('15:35:33.2302', '+17:39:19.999'),
                             ('15:36:28.1827', '+15:06:05.240'),
                             ('15:36:29.2391', '+16:07:08.705'),
                             ('15:40:59.1008', '+16:01:28.517'),
                             ('15:41:54.7132', '+18:27:50.532'),
                             ('15:44:42.1323', '+17:15:51.197'),
                             ('15:47:17.31882', '+14:06:55.2617'),
                             ('15:57:14.57093', '+14:24:52.1359'),
                             ('15:41:47.41474', '+12:50:51.0937'),
                             ('15:44:01.82075', '+02:30:54.634'),
                             ('15:50:17.54635', '+02:11:47.4362')
                             ])

draw_lines = get_reverse_map(
    [('iota', 'kappa'),
     ('kappa', 'gamma'),
     ('gamma', 'beta'),
     ('beta', 'iota'),
     ('beta', 'delta'),
     ('delta', 'alpha'),
     ('alpha', 'epsilon'),
     ('epsilon', 'omega'),
     ('omega', 'mu')
     ], star_names)

constellations(coordinates=serpens_coordinates, star_names=star_names, constellation_name='serpens',
               short_name='ser1', line_coordinates=draw_lines, turn_half=True)
# its short name is not based on 3 letters
