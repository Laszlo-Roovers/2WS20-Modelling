import numpy as np
from math import sqrt
from typing import Tuple


def setup(min_x: float, max_x: float,
          step: float) -> Tuple[np.ndarray, np.ndarray]:
    x = np.arange(min_x, max_x, step)
    y = np.empty(len(x))

    return x, y


def distribution_f(x) -> float:
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x
    else:
        return 1


def density_f(x) -> float:
    if x <= 0:
        return 0
    elif 0 < x < 1:
        return 1
    else:
        return 0


def density_kumaraswamy(x) -> float:
    if x <= 0:
        return 0
    elif 0 < x < 1:
        return 10*x*(1-x**2)**4
    else:
        return 0


def second_highest_bid(players: int, bid: float) -> float:
    if players == 3:
        if bid <= 0:
            return 0
        elif 0 < bid < 1:
            return 2 * bid * (1 - bid)
        else:
            return 0

    if players == 4:
        if bid <= 0:
            return 0
        elif 0 < bid < 1:
            return 3 * bid**2 * (1 - bid)
        else:
            return 0

    # General case. This could also replace the two cases above.
    if bid <= 0:
        return 0
    elif 0 < bid < 1:
        return players * bid**(players-1) - players * bid**players
    else:
        return 0


def reward_uniform(players, value):
    summand_1 = float(-1 * (-1 * value * players))
    summand_2 = sqrt(players**2 * value**2 + 2 * value * players**2 + 6 *
                      players - 2 * value * players - 3 * players**2 - 3)

    denominators = [summand_1 + summand_2, summand_1 - summand_2]
    numerator = float(2 * players - 2)

    result = []
    for denominator in denominators:
        result.append(denominator / numerator)

    return result


def reward_kumaraswamy(players, value):
    summand_1 = -1 *(-1*value*players)
    summand_2 = sqrt((-1*players*value - players + 1)**2 -4 * value * (
                      players - 1)**2)
    denominators = [summand_1 + summand_2, summand_1 - summand_2]
    numerator = float(2 * (players - 1))

    result = []
    for denominator in denominators:
        result.append(denominator / numerator)

    return result
