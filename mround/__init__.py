"""Rounding functions compatible with Python 2 and 3."""
from __future__ import absolute_import, division
from math import fabs, floor, ceil, copysign, modf

__version__ = "1.0"

def round_down(number, ndigits=0):
    """Round a number towards zero"""
    scale = 10 ** ndigits
    value = floor(fabs(number) * scale) / scale
    return copysign(value, number)

def round_up(number, ndigits=0):
    """Round a number away from zero"""
    scale = 10 ** ndigits
    value = ceil(fabs(number) * scale) / scale
    return copysign(value, number)

def round_half_up(number, ndigits=0):
    """Round a number to nearest with ties going away from zero.

    The behavior of this function is consistent with the built-in round
    function in Python 2.
    """
    scale = 10 ** ndigits
    value = floor((fabs(number) * scale) + 0.5) / scale
    return copysign(value, number)

def round_half_even(number, ndigits=0):
    """Round a number to nearest with ties going to nearest even.

    The behavior of this function is consistent with the built-in round
    function in Python 3. However, this function always returns a float.
    """
    # Could use from future.builtins import round as round_half_even
    scale = 10 ** ndigits
    val_1 = fabs(number) * scale
    fraction, integral = modf(val_1)

    if fraction > 0.5:
        val2 = ceil(val_1) / scale
    elif fraction == 0.5 and integral % 2 != 0:
        val2 = ceil(val_1) / scale
    else:
        val2 = floor(val_1) / scale

    return copysign(val2, number)
