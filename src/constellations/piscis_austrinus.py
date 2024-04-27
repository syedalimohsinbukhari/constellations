"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map

star_names = {0: 'alpha^A', 1: 'alpha^B', 2: 'beta', 3: 'gamma', 4: 'delta', 5: 'epsilon', 6: 'zeta', 7: 'eta',
              8: 'theta', 9: 'iota', 10: 'lambda', 11: 'mu', 12: 'pi', 13: 'tau', 14: 'upsilon'}

piscis_austrinus_coordinates = array([('22:57:39.04650', '-29:37:20.0500'), ('22:57:39.04650', '-29:37:20.0500'),
                                      ('22:31:30.33038', '-32:20:45.8653'), ('22:52:31.52285', '-32:52:31.7041'),
                                      ('22:55:56.90026', '-32:32:22.6335'), ('22:40:39.34075', '-27:02:37.0157'),
                                      ('22:30:53.77304', '-26:04:25.5068'), ('22:00:50.22454', '-28:27:13.4587'),
                                      ('21:47:44.14993', '-30:53:53.9027'), ('21:44:56.80900', '-33:01:32.8200'),
                                      ('22:14:18.75029', '-27:46:00.8756'), ('22:08:23.01477', '-32:59:18.3783'),
                                      ('23:03:29.81653', '-34:44:57.8827'), ('22:10:08.78048', '-32:32:54.2687'),
                                      ('22:08:25.93132', '-34:02:37.8248')])

draw_lines = get_reverse_map([('epsilon', 'tau'), ('tau', 'mu'), ('mu', 'beta'), ('beta', 'gamma'),
                              ('gamma', 'delta'), ('delta', 'alpha^A'), ('alpha^A', 'epsilon'), ('mu', 'theta'),
                              ('theta', 'iota'), ('iota', 'mu')], star_names)

constellations(coordinates=piscis_austrinus_coordinates, star_names=star_names, constellation_name='piscis_austrinus',
               short_name='psa', line_coordinates=draw_lines, turn_half=True)
