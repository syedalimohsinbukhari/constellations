"""Created on Sep 02 10:52:23 2022."""

from numpy import trunc


def hms2dd(hms_value):
    h, m, s = [float(i) for i in hms_value.split(':')]

    return h * 15 + (m / 4) + (s / 240)


def dms2dd(dms_value):
    d, m, s = [float(i) for i in dms_value.split(':')]

    if d < 0:
        m, s = float(f'-{m}'), float(f'-{s}')

    return d + m / 60 + s / 3600


def dd2dms(degree_decimal: float) -> str:
    _d = trunc(degree_decimal)
    _deg_residual = abs(degree_decimal - _d)

    __min = _deg_residual * 60
    _m = trunc(__min)
    _min_residual = abs(__min - _m)

    _s = round(_min_residual * 60, 4)

    _m, _s = [_m + 1, '00'] if _s == 60 else [_m, _s]
    if int(_s) == _s:
        _s = int(_s)

    return f'{int(_d)}:{int(_m)}:{_s}'
