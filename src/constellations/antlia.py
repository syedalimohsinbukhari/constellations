"""Created on Sep 03 03:38:00 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'delta', 2: 'epsilon', 3: 'zeta_1', 4: 'zeta_2', 5: 'eta', 6: 'theta', 7: 'iota'}

antlia_coordinates = array([('10:27:09.10313', '-31:04:03.9830'), ('10:29:35.37844', '-30:36:25.4413'),
                            ('09:29:14.71968', '-35:57:04.8074'), ('09:30:46.09678', '-31:53:21.1911'),
                            ('09:31:32.15879', '-31:52:18.5989'), ('09:58:52.27552', '-35:53:27.4977'),
                            ('09:44:12.09512', '-27:46:10.1011'), ('10:56:43.05097', '-37:08:15.9521')])

draw_lines = [(7, 0), (0, 2)]

constellations(coordinates=antlia_coordinates, star_names=star_names, constellation_name='antlia', short_name='ant',
               line_coordinates=draw_lines)
