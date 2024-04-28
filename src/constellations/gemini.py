"""Created on Sep 23 19:24:09 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha_A', 1: 'alpha_B', 2: 'alpha_C', 3: 'beta', 4: 'gamma', 5: 'delta', 6: 'epsilon', 7: 'zeta',
              8: 'eta^A', 9: 'eta_B', 10: 'theta', 11: 'iota', 12: 'kappa', 13: 'lambda', 14: 'mu', 15: 'nu', 16: 'xi',
              17: 'o', 18: 'pi', 19: 'rho^A', 20: 'rho_B', 21: 'rho_C', 22: 'sigma', 23: 'tau', 24: 'upsilon',
              25: 'phi', 26: 'chi', 27: 'omega'}

gemini_coordinates = array([('07:34:35.86300', '31:53:17.7900'), ('07:34:36.10000', '31:53:18.5700'),
                            ('07:34:37.58400', '31:53:17.8160'), ('07:45:18.94987', '28:01:34.3160'),
                            ('06:37:42.71050', '16:23:57.4095'), ('07:20:07.37978', '21:58:56.3377'),
                            ('06:43:55.92626', '25:07:52.0515'), ('07:04:06.53079', '20:34:13.0739'),
                            ('06:14:52.65700', '22:30:24.4800'), ('06:14:52.56900', '22:30:24.3100'),
                            ('06:25:47.33887', '33:57:40.5175'), ('07:25:43.59532', '27:47:53.0929'),
                            ('07:44:26.85357', '24:23:52.7872'), ('07:18:05.58012', '16:32:25.3964'),
                            ('06:22:57.62686', '22:30:48.8979'), ('06:28:57.78613', '20:12:43.6856'),
                            ('06:45:17.36432', '12:53:44.1311'), ('07:39:09.93286', '34:35:03.6443'),
                            ('07:47:30.32300', '33:24:56.5034'), ('07:29:06.71900', '31:47:04.3800'),
                            ('07:29:06.00000', '31:46:56.0000'), ('07:29:07.76900', '31:59:37.8400'),
                            ('07:43:18.72689', '28:53:00.6422'), ('07:11:08.37042', '30:14:42.5831'),
                            ('07:35:55.34970', '26:53:44.6751'), ('07:53:29.81390', '26:45:56.8252'),
                            ('08:03:31.08225', '27:47:39.6243'), ('07:02:24.78033', '24:12:55.6051')])

draw_lines = [(0, 23), (23, 10), (23, 11), (11, 24), (24, 3), (24, 12), (23, 6), (6, 15), (6, 14), (14, 8),
              (24, 5), (5, 13), (13, 16), (5, 7), (7, 4)]

constellations(coordinates=gemini_coordinates, star_names=star_names, constellation_name='Gemini', short_name='gem',
               line_coordinates=draw_lines)
