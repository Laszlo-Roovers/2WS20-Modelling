import numpy as np
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
