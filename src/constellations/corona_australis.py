"""Created on Sep 17 16:25:11 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta^1', 7: 'eta^2',
              8: 'theta', 9: 'kappa^1', 10: 'kappa^2', 11: 'lambda', 12: 'mu', 13: 'sigma'}

corona_australis_coordinates = array([('19:09:28.34097', '-37:54:16.1022'), ('19:10:01.75580', '-39:20:26.8644'),
                                      ('19:06:25.11014', '-37:03:48.3901'), ('19:08:20.96980', '-40:29:48.1155'),
                                      ('18:58:43.37714', '-37:06:26.4865'), ('19:03:06.87698', '-42:05:42.3858'),
                                      ('18:48:50.49216', '-43:40:48.1977'), ('18:49:34.99512', '-43:26:02.7458'),
                                      ('18:33:30.18626', '-42:18:45.0335'), ('18:33:23.08090', '-38:43:12.1660'),
                                      ('18:33:23.13075', '-38:43:33.5408'), ('18:43:46.94143', '-38:19:24.3941'),
                                      ('18:47:44.61759', '-40:24:22.1955'), ('18:24:18.24148', '-44:06:36.9008')])

draw_lines = [(0, 2), (0, 1), (1, 3), (3, 8)]

constellations(coordinates=corona_australis_coordinates, star_names=star_names, constellation_name='Corona Australis',
               short_name='cra', line_coordinates=draw_lines)
