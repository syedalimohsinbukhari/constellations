"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(['alpha',
#                                      'beta^1',
#                                      'beta^2',
#                                      'gamma^1',
#                                      'gamma^2',
#                                      'delta',
#                                      'epsilon',
#                                      'zeta',
#                                      'eta',
#                                      'theta^1',
#                                      'theta^2',
#                                      'iota',
#                                      'kappa^1',
#                                      'kappa^2',
#                                      'lambda',
#                                      'mu',
#                                      'nu^1',
#                                      'nu^2',
#                                      'xi^1',
#                                      'xi^2',
#                                      'o',
#                                      'pi',
#                                      'rho^1',
#                                      'rho^2',
#                                      'sigma',
#                                      'tau',
#                                      'upsilon',
#                                      'phi',
#                                      'chi^1',
#                                      'chi^2',
#                                      'chi^3',
#                                      'psi',
#                                      'omega'])
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta^1', 2: 'beta^2', 3: 'gamma^1', 4: 'gamma^2', 5: 'delta', 6: 'epsilon', 7: 'zeta',
              8: 'eta', 9: 'theta^1', 10: 'theta^2', 11: 'iota', 12: 'kappa^1', 13: 'kappa^2', 14: 'lambda', 15: 'mu',
              16: 'nu^1', 17: 'nu^2', 18: 'xi^1', 19: 'xi^2', 20: 'o', 21: 'pi', 22: 'rho^1', 23: 'rho^2', 24: 'sigma',
              25: 'tau', 26: 'upsilon', 27: 'phi', 28: 'chi^1', 29: 'chi^2', 30: 'chi^3', 31: 'psi', 32: 'omega'}

sagittarius_coordinates = array([('19:23:53.17483', '-40:36:57.3705'),
('19:22:38.29770', '-44:27:32.2458'),
('19:23:13.13745', '-44:47:59.2051'),
('18:05:01.22643', '-29:34:48.3222'),
('18:05:48.48810', '-30:25:26.7235'),
('18:20:59.64354', '-29:49:41.1659'),
('18:24:10.31840', '-34:23:04.6193'),
('19:02:36.73024', '-29:52:48.2279'),
('18:17:37.63505', '-36:45:42.0667'),
('19:59:44.17834', '-35:16:34.7049'),
('19:59:51.35684', '-34:41:52.0797'),
('19:55:15.69691', '-41:52:05.8388'),
('20:22:27.50366', '-42:02:58.3648'),
('20:23:53.17666', '-42:25:22.3376'),
('18:27:58.24072', '-25:25:18.1146'),
('18:13:45.8', '-21:03:32'),
('18:54:10.17695', '-22:44:41.4247'),
('18:55:07.14098', '-22:40:16.8185'),
('18:57:20.47670', '-20:39:22.8539'),
('18:57:43.79908', '-21:06:23.9613'),
('19:04:40.98177', '-21:44:29.3845'),
('19:09:45.83293', '-21:01:25.0103'),
('19:21:40.35942', '-17:50:49.9168'),
('19:21:50.89574', '-18:18:30.1996'),
('18:55:15.92650', '-26:17:48.2068'),
('19:06:56.40897', '-27:40:13.5189'),
('19:21:43.62284', '-15:57:18.0625'),
('18:45:39.38610', '-26:59:26.7944'),
('19:25:16.49013', '-24:30:30.8599'),
('19:25:16.49013', '-24:30:30.8599'),
('19:25:29.65949', '-23:57:44.8390'),
('19:15:32.42658', '-25:15:24.0569'),
('19:55:50.36255', '-26:17:57.6933')
])

draw_lines = get_reverse_map(
    [('rho^1', 'rho^2'), ('rho^2', 'pi'), ('pi', 'o'), ('o', 'xi^2'), ('pi', 'xi^2'),
     ('tau', 'sigma'), ('sigma', 'phi'), ('phi', 'delta'), ('delta', 'gamma^1'), ('gamma^1', 'epsilon'),
     ('epsilon', 'zeta'), ('zeta', 'tau'),
     ('phi', 'lambda'), ('lambda', 'delta'), ('delta', 'gamma^1'), ('epsilon', 'eta')], star_names)

constellations(coordinates=sagittarius_coordinates, star_names=star_names, constellation_name='sagittarius',
               short_name='sgr', line_coordinates=draw_lines, turn_half=True)