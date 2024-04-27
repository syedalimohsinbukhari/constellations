from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'omicron', 15: 'pi^1', 16: 'pi^2', 17: 'rho',
              18: 'sigma', 19: 'tau', 20: 'upsilon', 21: 'phi', 22: 'chi', 23: 'psi'}

pavo_coordinates = array([('23:04:45.65345', '+15:12:18.9617'), ('23:03:46.45746', '+28:04:58.0336'),
                          ('00:13:14.15123', '+15:11:00.9368'), ('00:08:23.25988', '+29:05:25.5520'),
                          ('21:44:11.15614', '+09:52:30.0311'), ('22:41:27.72072', '+10:49:52.9079'),
                          ('22:43:00.13743', '+30:13:16.4822'), ('22:10:11.98528', '+06:11:52.3078'),
                          ('22:07:00.66206', '+25:20:42.3761'), ('21:44:38.73440', '+25:38:42.1280'),
                          ('22:46:31.87786', '+23:33:56.3561'), ('22:50:00.19315', '+24:36:05.6984'),
                          ('22:05:40.75170', '+05:03:30.7201'), ('22:46:41.58118', '+12:10:22.3854'),
                          ('22:41:45.39893', '+29:18:27.5542'), ('22:09:13.61893', '+33:10:20.4778'),
                          ('22:09:59.24371', '+33:10:41.5976'), ('22:55:13.66706', '+08:48:58.2387'),
                          ('22:52:24.07496', '+09:50:08.3791'), ('23:20:38.24188', '+23:44:25.2098'),
                          ('23:25:22.78350', '+23:24:14.7606'), ('23:52:29.28762', '+19:07:13.0218'),
                          ('00:14:36.16451', '+20:12:24.1205'), ('23:57:45.52681', '+25:08:29.0480')])

draw_lines = get_reverse_map([('beta', 'alpha'), ('alpha', 'gamma'), ('alpha', 'zeta'), ('zeta', 'theta'),
                              ('theta', 'epsilon'), ('beta', 'mu'), ('mu', 'lambda'), ('lambda', 'iota'),
                              ('iota', 'kappa'), ('beta', 'eta'), ('eta', 'pi^1'), ('pi^1', 'pi^2')], star_names)

constellations(coordinates=pavo_coordinates, star_names=star_names, constellation_name='pegasus',
               short_name='peg', line_coordinates=draw_lines, turn_half=True)
