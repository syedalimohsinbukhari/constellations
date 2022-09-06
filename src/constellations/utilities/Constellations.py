"""Created on Sep 02 10:35:22 2022."""

import astropy.units as u
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord

from src.constellations.utilities.conversion import hms2dd, dms2dd


def draw_line(coordinates, start_ind, stop_ind, color='cyan'):
    start = coordinates[0][start_ind], coordinates[1][start_ind]
    stop = coordinates[0][stop_ind], coordinates[1][stop_ind]
    plt.plot([start[0], stop[0]], [start[1], stop[1]], color=color)


def constellations(coordinates, star_names, constellation_name, short_name, line_coordinates=None, turn_half=False):
    ra, dec = [hms2dd(i) for i in coordinates[:, 0]], [dms2dd(i) for i in coordinates[:, 1]]

    with open(f'./txt/{short_name.lower()}.txt') as f:
        ara = f.readlines()

    _ra_bounds = [hms2dd(j) for j in [i.split('|')[0].replace(' ', ':') for i in ara]]
    _dec_bounds = [float(i.split('|')[1]) for i in ara]

    c = SkyCoord(ra=ra * u.deg, dec=dec * u.deg)

    if turn_half:
        wrap_at = 180

        c2 = SkyCoord(ra=_ra_bounds * u.deg, dec=_dec_bounds * u.deg)
        _ra_bounds, _dec_bounds = c2.ra.wrap_at(wrap_at * u.deg).value, [i.value for i in c2.dec]
    else:
        wrap_at = 360

    ra, dec = c.ra.wrap_at(wrap_at * u.deg).value, [i.value for i in c.dec]

    stars = [rf'$\{i}$' if 'omicron' not in i else rf"${i.replace('omicron', 'o')}$" for i in star_names.values()]

    plt.figure(figsize=(8, 8))
    plt.plot(_ra_bounds, _dec_bounds, 'r:')
    plt.plot([_ra_bounds[0], _ra_bounds[-1]], [_dec_bounds[0], _dec_bounds[-1]], 'r:')
    [draw_line([ra, dec], i, j) for i, j in line_coordinates]
    [plt.plot(_ra, _dec, marker='*', ms=20, color='y') for _ra, _dec in zip(ra, dec)]
    [plt.text(i, j, k, horizontalalignment='center', verticalalignment='center') for i, j, k in zip(ra, dec, stars)]
    plt.title(f'{constellation_name.capitalize()} constellation')
    plt.xlabel('Right ascension\n[deg]')
    plt.ylabel('Declination\n[deg]')

    p = plt.gca().get_xticks()
    mask = [i < 0 for i in p]
    if any(mask):
        tl = [round(360 - abs(i), 2) if i < 0 else i for i in p]
        plt.gca().set_xticklabels(tl)

    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.savefig(rf'./pdfs/{constellation_name.lower()}.pdf')
    plt.savefig(rf'./pdfs/{constellation_name.lower()}.jpg')
    plt.close()
