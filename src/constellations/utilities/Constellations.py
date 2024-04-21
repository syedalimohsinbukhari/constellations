"""Created on Sep 02 10:35:22 2022."""
import string
from typing import Dict, List, Tuple

import astropy.units as u
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from numpy import ndarray

from .conversion import dms2dd, hms2dd


def draw_line(coordinates, start_ind, stop_ind, color='cyan'):
    start = coordinates[0][start_ind], coordinates[1][start_ind]
    stop = coordinates[0][stop_ind], coordinates[1][stop_ind]
    plt.plot([start[0], stop[0]], [start[1], stop[1]], color=color)


def constellations(coordinates: ndarray, star_names: Dict[int, str], constellation_name: str, short_name: str,
                   line_coordinates: List[Tuple[int, int]], turn_half: bool = False) -> None:
    """
    Plot the constellation given the coordinates and the star names.

    Parameters
    ----------
    coordinates : ndarray
        An array of right ascension and declination values for the stars in the constellation.
        The right ascension values should be in hours, minutes, and seconds, and the declination values should be in
        degrees, minutes, and seconds. The right ascension and declination values should be separated by a comma.
    star_names : Dict[int, str]
        A dictionary mapping the indices of the stars in the coordinates array to their names.
    constellation_name : str
        The IAU defined name of the constellation.
    short_name : str
        The IAU defined short name of the constellation.
    line_coordinates : List[Tuple[int, int]]
        A list of tuples containing the starting and ending indices for the lines connecting the stars in the
        constellation.
    turn_half : bool, optional
        Whether to turn half of the plot to match the conventions of the celestial sphere, by default False.

    Returns
    ----------
        None

    Notes
    ----------
        The right ascension values will be converted to degrees and the declination values will be left as is.
        The boundary lines of the constellation are taken from the IAU boundaries file for the given short name.
        The star chart will be saved as a PDF and a PNG file with the name of the constellation.
    """
    constellation_name = constellation_name.replace(' ', '_')

    ra, dec = [hms2dd(i) for i in coordinates[:, 0]], [dms2dd(i) for i in coordinates[:, 1]]

    with open(f'boundaries/{short_name.lower()}.txt') as f:
        iau_boundaries = f.readlines()

    _ra_bounds = [hms2dd(j) for j in [i.split('|')[0].replace(' ', ':') for i in iau_boundaries]]
    _dec_bounds = [float(i.split('|')[1]) for i in iau_boundaries]

    c = SkyCoord(ra=ra * u.deg, dec=dec * u.deg)

    if turn_half:
        wrap_at = 180

        c_boundaries = SkyCoord(ra=_ra_bounds * u.deg, dec=_dec_bounds * u.deg)
        _ra_bounds, _dec_bounds = c_boundaries.ra.wrap_at(wrap_at * u.deg).value, [i.value for i in c_boundaries.dec]
    else:
        wrap_at = 360

    ra, dec = c.ra.wrap_at(wrap_at * u.deg).value, [i.value for i in c.dec]

    alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    stars = [rf'$\{star_name_}$'
             if all(j != star_name_ for j in alphabets) and star_name_ != 'omicron' else
             'o' if star_name_ == 'omicron' else f'{star_name_}'
             for star_name_ in star_names.values()]

    plt.figure(figsize=(8, 8))
    plt.plot(_ra_bounds, _dec_bounds, 'r:')
    plt.plot([_ra_bounds[0], _ra_bounds[-1]], [_dec_bounds[0], _dec_bounds[-1]], 'r:')
    [draw_line([ra, dec], i, j) for i, j in line_coordinates]
    [plt.plot(_ra, _dec, marker='*', ms=20, color='y') for _ra, _dec in zip(ra, dec)]
    [plt.text(i, j, k, horizontalalignment='center', verticalalignment='center') for i, j, k in zip(ra, dec, stars)]
    plt.title(f"{constellation_name.replace('_', ' ').upper()} constellation")
    plt.xlabel('Right ascension\n[deg]')
    plt.ylabel('Declination\n[deg]')

    p = plt.gca().get_xticks()
    mask = [i < 0 for i in p]
    if any(mask):
        tl = [round(360 - abs(i), 2) if i < 0 else i for i in p]
        plt.gca().set_xticklabels(tl)

    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.savefig(rf'pdfs/{constellation_name.lower()}.pdf')
    plt.savefig(rf'pngs/{constellation_name.lower()}.png')
    plt.close()
