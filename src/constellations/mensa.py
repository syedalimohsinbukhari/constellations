"""Created on Nov 05 15:38:52 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu', 13: 'xi', 14: 'pi'}

mensa_coordinates = array([('06:10:14.47353', '-74:45:10.9583'), ('05:02:42.99847', '-71:18:51.4765'),
                           ('05:31:53.01393', '-76:20:27.4779'), ('04:17:59.27258', '-80:12:50.5073'),
                           ('07:25:38.09870', '-79:05:39.0878'), ('06:40:02.89197', '-80:48:48.9391'),
                           ('04:55:11.20309', '-74:56:12.6705'), ('06:56:34.47434', '-79:25:12.6918'),
                           ('05:35:36.17870', '-78:49:15.1290'), ('05:50:16.78570', '-79:21:40.9000'),
                           ('05:47:48.13340', '-72:42:08.0993'), ('04:43:03.96306', '-70:55:51.7147'),
                           ('04:20:58.07210', '-81:34:47.7190'), ('04:58:50.96791', '-82:28:13.8521'),
                           ('05:37:09.88684', '-80:28:08.8346')])

draw_lines = [(0, 0)]

constellations(coordinates=mensa_coordinates, star_names=star_names, constellation_name='Mensa', short_name='men',
               line_coordinates=draw_lines)
