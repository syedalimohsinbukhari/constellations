"""Created on Sep 05 14:56:33 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu^1', 12: 'mu^2', 13: 'nu', 14: 'xi', 15: 'omicron^1', 16: 'omicron^2',
              17: 'pi^1', 18: 'pi^2', 19: 'rho^1', 20: 'rho^2', 21: 'sigma^1', 22: 'sigma^2', 23: 'sigma^3', 24: 'tau',
              25: 'upsilon^1', 26: 'upsilon^2', 27: 'phi^1', 28: 'phi^2', 29: 'chi', 30: 'psi^1', 31: 'psi^2',
              32: 'omega^1', 33: 'omega^2'}

cancer_coordinates = array([('08:58:29.20420', '11:51:27.6490'), ('08:16:30.92060', '09:11:07.9610'),
                            ('08:43:17.14820', '21:28:06.6008'), ('08:44:41.09921', '18:09:15.5034'),
                            ('08:40:27.01010', '19:32:41.3243'), ('08:21:12.70000', '17:38:52.0000'),
                            ('08:32:42.49600', '20:26:28.1865'), ('08:31:35.73082', '18:05:39.9166'),
                            ('08:46:41.81988', '28:45:35.6190'), ('09:07:44.00000', '10:40:05.0000'),
                            ('08:20:32.13630', '24:01:20.3198'), ('08:06:18.39542', '22:38:07.7587'),
                            ('08:07:45.85581', '21:34:54.5325'), ('09:02:44.26543', '24:27:10.4902'),
                            ('09:09:21.53325', '22:02:43.6053'), ('08:57:14.95026', '15:19:21.9512'),
                            ('08:57:35.20006', '15:34:52.6145'), ('09:12:17.54871', '14:59:45.7382'),
                            ('09:15:13.85196', '14:56:29.4401'), ('08:52:35.81110', '28:19:50.9550'),
                            ('08:55:39.68055', '27:55:38.9299'), ('08:52:34.62123', '32:28:26.9664'),
                            ('08:56:56.59711', '32:54:37.5423'), ('08:59:32.65432', '32:25:06.8093'),
                            ('09:08:00.04963', '29:39:15.2428'), ('08:31:30.51925', '24:04:51.9890'),
                            ('08:33:00.10385', '24:05:05.2560'), ('08:26:27.70615', '27:53:36.8867'),
                            ('08:26:47.06931', '26:56:07.7515'), ('08:20:03.86070', '27:13:03.7464'),
                            ('08:10:13.10700', '25:50:40.1300'), ('08:10:27.18056', '25:30:26.4061'),
                            ('08:00:55.87305', '25:23:34.2160'), ('08:01:43.75679', '25:05:22.0823')])

draw_lines = [(0, 3), (3, 1), (3, 2), (2, 8)]

constellations(coordinates=cancer_coordinates, star_names=star_names, constellation_name='Cancer', short_name='cnc',
               line_coordinates=draw_lines)
