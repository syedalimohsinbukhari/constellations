"""Created on Sep 24 09:13:47 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa^2', 10: 'mu', 11: 'nu', 12: 'omicron', 13: 'pi', 14: 'rho'}

indus_coordinates = array([('20:37:34.03201', '-47:17:29.4026'), ('20:54:48.60278', '-58:27:14.9618'),
                           ('21:26:15.43919', '-54:39:37.6515'), ('21:57:55.07353', '-54:59:33.2740'),
                           ('22:03:21.65423', '-56:47:09.5370'), ('20:49:28.96165', '-46:13:36.6083'),
                           ('20:44:02.33404', '-51:55:15.4970'), ('21:19:51.98955', '-53:26:57.9315'),
                           ('20:51:30.05098', '-51:36:29.4428'), ('22:05:51.01601', '-59:38:09.8597'),
                           ('21:05:14.24873', '-54:43:37.3496'), ('22:24:36.88538', '-72:15:19.4882'),
                           ('21:50:47.17512', '-69:37:45.7464'), ('21:56:14.05642', '-57:53:58.5155'),
                           ('22:54:39.48200', '-70:04:25.3500')])

draw_lines = [(0, 1), (1, 3), (3, 7), (7, 0)]

constellations(coordinates=indus_coordinates, star_names=star_names, constellation_name='Indus', short_name='ind',
               line_coordinates=draw_lines)
