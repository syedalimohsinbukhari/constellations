"""Created on Sep 02 10:52:23 2022."""

from numpy import trunc


def hms2dd(hms_value: str) -> float:
    """
    Convert an hour, minute, second value to a decimal degree value.

    Parameters
    ----------
    hms_value : str
        The hour, minute, second value to convert. The value must be in the format "h:m:s", where "h" is the hour value,
        "m" is the minute value, and "s" is the second value.

    Returns
    -------
    float
        The decimal degree value.

    Examples
    --------
    >>> hms2dd("8:45:12")
    127.75333333333333
    """
    h, m, s = [float(i) for i in hms_value.split(':')]
    return h * 15 + m / 4 + s / 240


def dms2dd(dms_value: str) -> float:
    """
    Convert a degree, minute, second value to a decimal degree value.

    Parameters
    ----------
    dms_value : str
        The degree, minute, second value to convert. The value must be in the format "d:m:s", where "d" is the degree
        value, "m" is the minute value, and "s" is the second value.

    Returns
    -------
    float
        The decimal degree value.

    Examples
    --------
    >>> dms2dd("30:45:12")
    30.75333333333333
    """
    d, m, s = [float(i) for i in dms_value.split(':')]

    if d < 0:
        m, s = float(f'-{m}'), float(f'-{s}')

    return d + m / 60 + s / 3600


def dd2dms(degree_decimal: float) -> str:
    """
    Convert a decimal degree value to an hour, minute, second value.

    Parameters
    ----------
    degree_decimal : float
        The decimal degree value to convert.

    Returns
    -------
    str
        The hour, minute, second value. The value is returned in the format "h:m:s", where "h" is the hour value,
        "m" is the minute value, and "s" is the second value.

    Examples
    --------
    >>> dd2dms(127.75333333333333)
    '8:45:12'
    """
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
