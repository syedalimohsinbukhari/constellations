"""Created on Sep 23 01:00:28 2022."""
from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon'}

equuleus_coordinates = array([('21:15:49.43192', '05:14:52.2430'), ('21:22:53.61365', '06:48:40.1125'),
                              ('21:10:20.50005', '10:07:53.6763'), ('21:14:28.81531', '10:00:25.1259'),
                              ('20:59:04.47539', '04:17:36.5211')])

draw_lines = [(0, 3), (3, 2)]

constellations(coordinates=equuleus_coordinates, star_names=star_names, constellation_name='Equuleus', short_name='equ',
               line_coordinates=draw_lines)
