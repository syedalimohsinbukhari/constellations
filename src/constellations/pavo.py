from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu^1', 12: 'mu^2', 13: 'nu', 14: 'xi', 15: 'omicron', 16: 'pi', 17: 'rho',
              18: 'sigma', 19: 'tau', 20: 'upsilon', 21: 'phi^1', 22: 'phi^2', 23: 'omega'}

# iota and some other stars do not directly mentioned RA and DEC directly.
# According to wiki, its a list of stars. But I'm not sure.

pavo_coordinates = array([('20:25:38.85705', '-56:44:06.3230'), ('20:44:57.49399', '-66:12:11.5708'),
                          ('21:26:26.60484', '-65:21:58.3145'), ('20:08:43.60887', '-66:10:55.4428'),
                          ('20:00:35.55558', '-72:54:37.8198'), ('18:43:02.13528', '-71:25:41.2065'),
                          ('17:45:43.98605', '-64:43:25.9394'), ('18:48:37.90451', '-65:04:39.6498'),
                          ('18:10:26.26000', '-62:00:10.0000'), ('18:56:57.02788', '-67:14:00.5831'),
                          ('18:52:13.03427', '-62:11:15.3324'), ('20:00:23.11000', '-66:56:56.0000'),
                          ('20:01:52.40000', '-66:56:37.7000'), ('18:31:22.42509', '-62:16:41.8853'),
                          ('18:23:13.64610', '-61:29:37.9364'), ('21:13:20.44000', '-70:07:34.4000'),
                          ('18:08:34.81459', '-63:40:06.7906'), ('20:37:35.31275', '-61:31:47.7145'),
                          ('20:37:35.24000', '-61:31:47.1000'), ('20:49:18.28000', '-68:46:35.0000'),
                          ('19:16:28.60000', '-69:11:26.7000'), ('20:41:57.06000', '-66:45:38.3000'),
                          ('20:35:34.84931', '-60:34:54.3103'), ('20:40:02.63822', '-60:32:56.0200')])

draw_lines = get_reverse_map([('alpha', 'delta'), ('delta', 'mu^1'), ('mu^1', 'mu^2'), ('mu^2', 'zeta'),
                              ('alpha', 'gamma'), ('gamma', 'beta'), ('beta', 'delta'), ('delta', 'epsilon'),
                              ('delta', 'kappa'), ('kappa', 'pi'), ('delta', 'lambda'), ('lambda', 'xi'),
                              ('xi', 'pi'), ('pi', 'eta')], star_names)

constellations(coordinates=pavo_coordinates, star_names=star_names, constellation_name='pavo',
               short_name='pav', line_coordinates=draw_lines)
