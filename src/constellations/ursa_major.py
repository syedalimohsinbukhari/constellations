"""Created on Apr 21 16:27:25 2024"""

from numpy import array

from src.constellations.perseus import perseus_coordinates
from src.constellations.utilities.Constellations import constellations
from src.constellations.utilities.others_ import get_reverse_map, create_star_dictionary

# star_names = create_star_dictionary(
#     ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
#      'o', 'pi^1', 'pi^2', 'rho', 'sigma^1', 'sigma^2', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
#     )
#
# print(star_names)

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'o', 15: 'pi^1', 16: 'pi^2', 17: 'rho',
              18: 'sigma^1', 19: 'sigma^2', 20: 'tau', 21: 'upsilon', 22: 'phi', 23: 'chi', 24: 'psi', 25: 'omega'}

ursa_major_coordinates = array([('11:03:43.67152', '+61:45:03.7249'),
                                ('11:01:50.47654', '+56:22:56.7339'),
                                ('11:53:49.84732', '+53:41:41.1350'),
                                ('12:15:25.56063', '+57:01:57.4156'),
                                ('12:54:01.74959', '+55:57:35.3627'),
                                ('13:23:55.54048', '+54:55:31.2671'),
                                ('13:47:32.43776', '+49:18:47.7602'),
                                ('09:32:51.43390', '+51:40:38.2811'),
                                ('08:59:12.45362', '+48:02:30.5741'),
                                ('09:03:37.52762', '+47:09:23.4890'),
                                ('10:17:05.78287', '+42:54:51.6808'),
                                ('10:22:19.73976', '+41:29:58.2691'),
                                ('11:18:28.73664', '+33:05:39.5107'),
                                ('11:18:10.902', '+31:31:44.98'),
                                ('08:30:15.87064', '+60:43:05.4115'),
                                ('08:39:11.70440', '+65:01:15.2667'),
                                ('08:40:12.81767', '+64:19:40.5700'),
                                ('09:02:32.69092', '+67:37:46.6280'),
                                ('09:08:23.49946', '+66:52:23.6492'),
                                ('09:10:23.538', '+67:08:02.44'),
                                ('09:10:55.06553', '+63:30:49.0553'),
                                ('09:50:59.35700', '+59:02:19.4486'),
                                ('09:52:06.35437', '+54:03:51.5962'),
                                ('11:46:03.01407', '+47:46:45.8626'),
                                ('11:09:39.80868', '+44:29:54.5520'),
                                ('10:53:58.74035', '+43:11:23.8483')
                                ])

draw_lines = get_reverse_map(
    [('eta', 'zeta'), ('zeta', 'epsilon'), ('epsilon', 'delta'), ('delta', 'alpha'), ('alpha', 'beta'),
     ('beta', 'gamma'), ('gamma', 'delta'), ('alpha', 'o'), ('o', 'upsilon'), ('upsilon', 'beta'), ('gamma', 'chi'),
     ('chi', 'psi'), ('psi', 'mu'), ('mu', 'lambda'), ('chi', 'nu'), ('nu', 'xi')
     ], star_names)

constellations(coordinates=ursa_major_coordinates, star_names=star_names, constellation_name='ursa_major',
               short_name='uma', line_coordinates=draw_lines, turn_half=True)
