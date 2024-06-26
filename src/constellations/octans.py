"""Created on Mar 25 23:52:38 2024."""
from numpy import array

from src.constellations.utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma^1', 3: 'gamma^2', 4: 'gamma^3', 5: 'delta', 6: 'epsilon', 7: 'zeta',
              8: 'eta', 9: 'theta', 10: 'iota', 11: 'kappa', 12: 'lambda', 13: 'mu^1', 14: 'mu^2', 15: 'nu', 16: 'xi',
              17: 'pi^1', 18: 'pi^2', 19: 'rho', 20: 'sigma', 21: 'tau', 22: 'upsilon', 23: 'phi', 24: 'chi', 25: 'psi',
              26: 'omega'}

octans_coordinates = array([('21:04:43.06347', '-77:01:25.5735'), ('22:46:03.51098', '-81:22:53.8120'),
                            ('23:52:06.48895', '-82:01:07.7489'), ('23:57:32.86170', '-82:10:11.3096'),
                            ('00:10:02.17249', '-82:13:26.5695'), ('14:26:55.23244', '-83:40:04.3868'),
                            ('22:20:01.67970', '-80:26:23.0947'), ('08:56:40.97572', '-85:39:47.3476'),
                            ('10:59:13.75780', '-84:35:38.0177'), ('00:01:35.70158', '-77:03:56.6092'),
                            ('12:54:58.80949', '-85:07:24.1041'), ('13:40:55.48330', '-85:47:09.7520'),
                            ('21:50:54.56355', '-82:43:08.0450'), ('20:42:02.98730', '-76:10:50.1310'),
                            ('20:41:44.10200', '-75:21:02.8800'), ('21:41:28.64977', '-77:23:24.1563'),
                            ('22:50:22.81390', '-80:07:25.8418'), ('15:01:50.79830', '-83:13:39.5303'),
                            ('15:04:46.92320', '-83:02:17.9200'), ('15:43:16.92700', '-84:27:54.9900'),
                            ('21:08:46.86357', '-88:57:23.3983'), ('23:28:03.78550', '-87:28:55.9670'),
                            ('22:31:37.51520', '-85:58:02.1104'), ('18:23:36.44874', '-75:02:39.3975'),
                            ('18:54:47.14062', '-87:36:21.0359'), ('22:17:50.5954', '-77:30:41.599'),
                            ('15:11:08.79214', '-84:47:16.0295')])

draw_lines = [(5, 1), (1, 15), (15, 5)]

constellations(coordinates=octans_coordinates, star_names=star_names, constellation_name='octans', short_name='oct',
               line_coordinates=draw_lines)
