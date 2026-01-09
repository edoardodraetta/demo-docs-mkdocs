"""Statistical operations module.

This module provides basic statistical functions for data analysis.
"""

from typing import List, Union
import math


def mean(values: List[Union[int, float]]) -> float:
    """Calculate the arithmetic mean of a list of numbers.

    The mean is calculated as the sum of all values divided by the count.

    Args:
        values: A list of numeric values

    Returns:
        The arithmetic mean as a float

    Raises:
        ValueError: If the input list is empty

    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
        >>> mean([10, 20, 30])
        20.0
    """
    if not values:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(values) / len(values)


def variance(values: List[Union[int, float]]) -> float:
    """Calculate the population variance of a list of numbers.

    Variance measures how far numbers in a dataset are spread out
    from their average value.

    Args:
        values: A list of numeric values

    Returns:
        The population variance

    Raises:
        ValueError: If the input list is empty

    Note:
        This calculates population variance (dividing by N), not sample
        variance (dividing by N-1).

    Examples:
        >>> variance([1, 2, 3, 4, 5])
        2.0
    """
    if not values:
        raise ValueError("Cannot calculate variance of empty list")

    avg = mean(values)
    return sum((x - avg) ** 2 for x in values) / len(values)


def standard_deviation(values: List[Union[int, float]]) -> float:
    """Calculate the standard deviation of a list of numbers.

    Standard deviation is the square root of variance and provides a measure
    of spread in the same units as the original data.

    Args:
        values: A list of numeric values

    Returns:
        The standard deviation

    Raises:
        ValueError: If the input list is empty

    See Also:
        variance: For the variance calculation

    Examples:
        >>> round(standard_deviation([1, 2, 3, 4, 5]), 2)
        1.41
    """
    return math.sqrt(variance(values))
