"""Created on Sep 28 19:23:21 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa^1', 10: 'kappa^2', 11: 'lambda', 12: 'mu', 13: 'nu^1', 14: 'nu^2', 15: 'xi^1', 16: 'xi^2',
              17: 'omicron', 18: 'pi', 19: 'rho', 20: 'sigma', 21: 'tau^1', 22: 'tau^2', 23: 'upsilon', 24: 'phi^1',
              25: 'phi^2', 26: 'chi', 27: 'psi^1', 28: 'psi^2', 29: 'omega'}

lupus_coordinates = array([('14:41:55.75579', '-47:23:17.5155'), ('14:58:31.92536', '-43:08:02.2699'),
                           ('15:35:08.44835', '-41:10:00.3247'), ('15:21:22.32168', '-40:38:51.0738'),
                           ('15:22:40.86826', '-44:41:22.6146'), ('15:12:17.09595', '-52:05:57.2919'),
                           ('16:00:07.32786', '-38:23:48.1513'), ('16:06:35.54525', '-36:48:08.2653'),
                           ('14:19:24.22219', '-46:03:29.1437'), ('15:11:56.07286', '-48:44:16.1692'),
                           ('15:11:57.67549', '-48:44:37.3397'), ('15:08:50.61639', '-45:16:47.4950'),
                           ('15:18:32.02296', '-47:52:30.9957'), ('15:22:08.27124', '-47:55:40.0543'),
                           ('15:21:48.15000', '-48:19:03.4600'), ('15:56:53.49808', '-33:57:58.0129'),
                           ('15:56:54.12100', '-33:57:51.3448'), ('14:51:38.30289', '-43:34:31.2956'),
                           ('15:05:07.08596', '-47:03:04.4976'), ('14:37:53.22583', '-49:25:32.9798'),
                           ('14:32:37.05667', '-50:27:25.7746'), ('14:26:08.22424', '-45:13:17.1315'),
                           ('14:26:10.81378', '-45:22:45.4023'), ('15:24:45.00855', '-39:42:36.9524'),
                           ('15:21:48.36967', '-36:15:40.9525'), ('15:23:09.35005', '-36:51:30.5521'),
                           ('15:50:57.53760', '-33:37:37.7960'), ('15:39:45.97931', '-34:24:42.9073'),
                           ('15:42:41.02206', '-34:42:37.4617'), ('15:38:03.20372', '-42:34:02.4444')])

draw_lines = [(0, 5), (5, 6), (6, 26), (26, 24), (24, 6), (6, 2), (2, 4), (4, 5), (2, 3), (3, 1)]

constellations(coordinates=lupus_coordinates, star_names=star_names, constellation_name='Lupus', short_name='lup',
               line_coordinates=draw_lines)
