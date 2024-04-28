from numpy import array

from utilities.Constellations import constellations
from utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'zeta', 5: 'eta^1', 6: 'eta^2', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'mu_dor'}

pictor_coordinates = array([('06:48:11.45512', '-61:56:29.0008'), ('05:47:17.10000', '-51:03:59.0000'),
                            ('05:49:49.66181', '-56:09:59.9808'), ('06:10:17.90800', '-54:58:07.1100'),
                            ('05:19:22.13548', '-50:36:21.4820'), ('05:02:48.68641', '-49:09:05.0644'),
                            ('05:04:58.01433', '-49:34:40.2034'), ('05:24:46.28819', '-52:18:58.4836'),
                            ('04:50:55.32684', '-53:27:41.2300'), ('05:22:22.14661', '-56:08:03.8409'),
                            ('04:42:46.42350', '-50:28:52.8050'), ('06:31:58.31021', '-58:45:13.8117'),
                            ('06:22:55.82671', '-56:22:11.8909'), ('06:07:03.40671', '-62:09:16.4496')])

draw_lines = get_reverse_map([('beta', 'gamma'), ('gamma', 'alpha')], star_names)

constellations(coordinates=pictor_coordinates, star_names=star_names, constellation_name='pictor',
               short_name='pic', line_coordinates=draw_lines, turn_half=True)
