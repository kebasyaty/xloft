"""Convert an integer to Roman and vice versa.

The module contains the following functions:

- `int_to_roman` - Convert an integer to Roman.
- `roman_to_int` - Convert to integer from Roman.
"""

from __future__ import annotations

__all__ = (
    "int_to_roman",
    "roman_to_int",
)

ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def int_to_roman(number: int) -> str:
    """Convert an integer to Roman.

    Examples:
        >>> from xloft import int_to_roman
        >>> int_to_roman(1994)
        MCMXCIV

    Args:
        number (int): Integer.

    Returns:
        Roman numeral string.
    """
    result = ""
    for arabic, roman in ROMAN:
        (factor, number) = divmod(number, arabic)
        result += roman * factor
    return result


def roman_to_int(roman: str) -> int:
    """Convert to integer from Roman.

    Examples:
        >>> from xloft import roman_to_int
        >>> roman_to_int("MCMXCIV")
        1994

    Args:
        roman (str): Roman numeral string.

    Returns:
        Integer.
    """
    i_count = roman.count("I")
    v_count = roman.count("V")
    x_count = roman.count("X")
    l_count = roman.count("L")
    c_count = roman.count("C")
    d_count = roman.count("D")
    m_count = roman.count("M")

    iv_count = roman.count("IV")
    i_count -= iv_count
    v_count -= iv_count

    ix_count = roman.count("IX")
    i_count -= ix_count
    x_count -= ix_count

    xl_count = roman.count("XL")
    x_count -= xl_count
    l_count -= xl_count

    xc_count = roman.count("XC")
    x_count -= xc_count
    c_count -= xc_count

    cd_count = roman.count("CD")
    c_count -= cd_count
    d_count -= cd_count

    cm_count = roman.count("CM")
    c_count -= cm_count
    m_count -= cm_count

    total = 0
    total += 1 * i_count
    total += 5 * v_count
    total += 10 * x_count
    total += 50 * l_count
    total += 100 * c_count
    total += 500 * d_count
    total += 1000 * m_count

    total += 4 * iv_count
    total += 9 * ix_count
    total += 40 * xl_count
    total += 90 * xc_count
    total += 400 * cd_count
    total += 900 * cm_count

    return total
