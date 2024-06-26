"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta^1', 'delta^2', 'delta^3', 'epsilon', 'zeta', 'eta', 'theta^1', 'theta^2', 'iota',
#      'kappa^1', 'kappa^2', 'lambda', 'mu', 'nu', 'xi', 'o', 'pi', 'rho', 'sigma^1', 'sigma^2', 'tau', 'upsilon',
#      'phi', 'chi', 'psi', 'omega^1', 'omega^2']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta^1', 4: 'delta^2', 5: 'delta^3', 6: 'epsilon', 7: 'zeta',
              8: 'eta', 9: 'theta^1', 10: 'theta^2', 11: 'iota', 12: 'kappa^1', 13: 'kappa^2', 14: 'lambda', 15: 'mu',
              16: 'nu', 17: 'xi', 18: 'o', 19: 'pi', 20: 'rho', 21: 'sigma^1', 22: 'sigma^2', 23: 'tau', 24: 'upsilon',
              25: 'phi', 26: 'chi', 27: 'psi', 28: 'omega^1', 29: 'omega^2'}

taurus_coordinates = array([('04:35:55.23907', '+16:30:33.4885'),
                            ('05:26:17.51312', '+28:36:26.8262'),
                            ('04:19:47.6037', '+15:37:39.512'),
                            ('04:22:56.09253', '+17:32:33.0487'),
                            ('04:24:05.75985', '+17:26:38.8583'),
                            ('04:25:29.38340', '+17:55:40.4579'),
                            ('04:28:37.0003', '+19:10:49.563'),
                            ('05:37:38.68542', '+21:08:33.1588'),
                            ('03:47:29.077', '+24:06:18.49'),
                            ('04:28:34.49603', '+15:57:43.8494'),
                            ('05:03:05.74725', '+21:35:23.8627'),
                            ('04:25:22.16505', '+22:17:37.9375'),
                            ('04:00:40.81572', '+12:29:25.2259'),
                            ('04:15:32.05687', '+08:53:32.4916'),
                            ('04:03:09.37966', '+05:59:21.4792'),
                            ('03:27:10.151', '+09:43:57.63'),
                            ('03:24:48.79146', '+09:01:43.9941'),
                            ('04:26:36.37093', '+14:42:49.6126'),
                            ('04:33:50.91753', '+14:50:39.9232'),
                            ('04:39:09.22247', '+15:47:59.5345'),
                            ('04:42:14.70161', '+22:57:24.9214'),
                            ('04:26:18.46368', '+22:48:48.8885'),
                            ('04:20:21.21580', '+27:21:02.7009'),
                            ('04:22:34.944', '+25:37:45.53'),
                            ('04:07:00.45697', '+29:00:04.7084'),
                            ('02:12:22.28003', '+30:18:11.043'),
                            ('04:17:15.66155', '+20:34:42.934')

                            ])

draw_lines = get_reverse_map(
    [('beta', 'epsilon'), ('epsilon', 'delta^1'), ('delta^1', 'delta^2'), ('delta^2', 'gamma'), ('zeta', 'alpha'),
     ('alpha', 'theta'), ('theta', 'gamma'), ('gamma', 'lambda'), ('lambda', 'xi'), ('xi', 'nu')], star_names)

constellations(coordinates=taurus_coordinates, star_names=star_names, constellation_name='taurus',
               short_name='tau', line_coordinates=draw_lines, turn_half=True)
