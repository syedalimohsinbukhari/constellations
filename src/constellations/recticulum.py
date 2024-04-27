"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta^1', 6: 'zeta^2', 7: 'eta',
              8: 'theta', 9: 'iota', 10: 'kappa'}

recticulum_coordinates = array([('04:14:25.48414', '-62:28:25.8917'), ('03:44:11.97587', '-64:48:24.8610'),
                                ('04:00:53.80860', '-62:09:33.4250'), ('03:58:44.74945', '-61:24:00.6673'),
                                ('04:16:29.02800', '-59:18:07.7600'), ('03:17:46.16331', '-62:34:31.1541'),
                                ('04:21:53.32714', '-63:23:11.0072'), ('04:17:40.27169', '-63:15:19.4882'),
                                ('04:01:18.15162', '-61:04:43.7559'), ('03:29:22.67724', '-62:56:15.0991')])

draw_lines = get_reverse_map([('epsilon', 'iota'), ('iota', 'delta'), ('delta', 'beta'), ('beta', 'alpha'),
                              ('alpha', 'epsilon')], star_names)

constellations(coordinates=recticulum_coordinates, star_names=star_names, constellation_name='recticulum',
               short_name='ret', line_coordinates=draw_lines, turn_half=True)
