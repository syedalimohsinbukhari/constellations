"""Created on Mar 25 23:39:41 2024."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'gamma^1', 1: 'gamma^2', 2: 'delta', 3: 'epsilon', 4: 'zeta', 5: 'eta', 6: 'theta', 7: 'iota^1',
              8: 'iota^2', 9: 'kappa', 10: 'lambda', 11: 'mu'}

norma_coordinates = array([('16:17:00.93411', '-50:04:05.2333'), ('16:19:50.42227', '-50:09:19.8223'),
                           ('16:06:29.43692', '-45:10:23.4518'), ('16:27:11.03611', '-47:33:17.2226'),
                           ('16:13:22.69800', '-55:32:27.4108'), ('16:03:12.89783', '-49:13:46.9151'),
                           ('16:15:15.31794', '-47:22:19.2710'), ('16:03:32.08942', '-57:46:30.2641'),
                           ('16:09:18.54876', '-57:56:03.5420'), ('16:13:28.72874', '-54:37:49.6860'),
                           ('16:19:17.64660', '-42:40:26.3014'), ('16:34:05.02028', '-44:02:43.1281')])

draw_lines = [(1, 3), (3, 2), (2, 5), (5, 1)]

constellations(coordinates=norma_coordinates, star_names=star_names, constellation_name='Norma', short_name='nor',
               line_coordinates=draw_lines)
