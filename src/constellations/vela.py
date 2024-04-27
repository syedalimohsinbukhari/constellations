"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'gamma', 1: 'delta', 2: 'kappa', 3: 'lambda', 4: 'mu', 5: 'o', 6: 'phi', 7: 'psi'}

vela_coordinates = array([('08:09:31.95013', '-47:20:11.7108'), ('08:44:42.22600', '-54:42:31.7600'),
                          ('09:22:06.81761', '-55:00:38.4017'), ('09:07:59.75787', '-43:25:57.3273'),
                          ('10:46:46.17877', '-49:25:12.9244'), ('08:40:17.58553', '-52:55:18.8002'),
                          ('09:56:51.74200', '-54:34:04.0400'), ('09:30:41.99958', '-40:28:00.2616')])

draw_lines = get_reverse_map([('psi', 'lambda'), ('lambda', 'gamma'), ('gamma', 'delta'), ('delta', 'kappa'),
                              ('kappa', 'phi'), ('phi', 'mu'), ('mu', 'psi')], star_names)

constellations(coordinates=vela_coordinates, star_names=star_names, constellation_name='vela',
               short_name='vel', line_coordinates=draw_lines, turn_half=True)
