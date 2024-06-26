"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'delta', 'epsilon', 'zeta^1', 'zeta^2', 'eta', 'theta', 'iota^1', 'iota^2', 'kappa', 'lambda',
#      'mu^1', 'mu^2', 'nu', 'xi', 'o', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'chi', 'psi', 'omega^1', 'omega^2',
#      'G', 'H', 'N', 'Q'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'delta', 3: 'epsilon', 4: 'zeta^1', 5: 'zeta^2', 6: 'eta', 7: 'theta',
              8: 'iota^1', 9: 'iota^2', 10: 'kappa', 11: 'lambda', 12: 'mu^1', 13: 'mu^2', 14: 'nu', 15: 'xi', 16: 'o',
              17: 'pi', 18: 'rho', 19: 'sigma', 20: 'tau', 21: 'upsilon', 22: 'chi', 23: 'psi', 24: 'omega^1',
              25: 'omega^2', 26: 'G', 27: 'H', 28: 'N', 29: 'Q'}

scorpius_coordinates = array([('16:29:24.45970', '-26:25:55.2094'),
                              ('16:05:26.23198', '-19:48:19.6300'),
                              ('16:00:20.00528', '-22:37:18.1431'),
                              ('16:50:09.8', '-34:17:36'),
                              ('16:53:59.727', '-42:21:43.31'),
                              ('16:54:35.00435', '-42:21:40.7407'),
                              ('17:12:09.19565', '-43:14:21.0905'),
                              ('17:37:19.12985', '-42:59:52.1808'),
                              ('17:47:35.08113', '-40:07:37.1893'),
                              ('17:50:11.11291', '-40:05:25.5629'),
                              ('17:42:29.27520', '-39:01:47.9391'),
                              ('17:33:36.520', '-37:06:13.76'),
                              ('16:51:52.23111', '-38:02:50.5694'),
                              ('16:52:20.14532', '-38:01:03.1258'),
                              ('16:11:59.740', '-19:27:38.33'),
                              ('16:04:22.191', '-11:22:22.60'),
                              ('16:20:38.18068', '-24:10:09.5491'),
                              ('15:58:51.11324', '-26:06:50.7886'),
                              ('15:56:53.07624', '-29:12:50.6612'),
                              ('16:21:11.31571', '-25:35:34.0515'),
                              ('16:35:52.95285', '-28:12:57.6615'),
                              ('17:30:45.83712', '-37:17:44.9285'),
                              ('16:13:50.906', '-11:50:15.89'),
                              ('16:12:00.01043', '-10:03:50.8353'),
                              ('16:06:48.42692', '-20:40:09.0902'),
                              ('16:07:24.32818', '-20:52:07.5518'),
                              ('17:49:51.48081', '-37:02:35.8975'),
                              ('16:36:22.47192', '-35:15:19.1803'),
                              ('16:31:22.93300', '-34:42:15.7146'),
                              ('17:36:32.85514', '-38:38:06.8918')
                              ])

draw_lines = get_reverse_map(
    [('nu', 'beta'),
     ('beta', 'delta'),
     ('delta', 'pi'),
     ('pi', 'rho'),
     ('delta', 'sigma'),
     ('sigma', 'alpha'),
     ('alpha', 'tau'),
     ('tau', 'epsilon'),
     ('epsilon', 'mu^1'),
     ('mu^1', 'mu^2'),
     ('mu^2', 'zeta^1'),
     ('zeta^1', 'zeta^2'),
     ('zeta^2', 'eta'),
     ('eta', 'theta'),
     ('theta', 'iota^1'),
     ('iota^1', 'kappa'),
     ('kappa', 'upsilon'),
     ('upsilon', 'lambda')
     ], star_names)

constellations(coordinates=scorpius_coordinates, star_names=star_names, constellation_name='scorpius',
               short_name='sco', line_coordinates=draw_lines, turn_half=True)
