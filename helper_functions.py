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
