import math
from typing import Union


def solve_quadratic_equation(a: float,
                             b: float,
                             c: float) -> Union[None, float, tuple[float, float]]:
    """
    Calculates the solutions to a quadratic equation of the form ax^2 + bx + c = 0.

    Args:
        a (float): The coefficient of x^2.
        b (float): The coefficient of x.
        c (float): The constant term.

    Returns:
        Union[None, float, Tuple[float, float]]: The solutions to the quadratic equation.
            - If there are no real solutions, returns None.
            - If there is a single real solution, returns the solution as a float.
            - If there are two real solutions, returns the solutions as a tuple of floats.
    """
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        x = -b / (2 * a)
        return x
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2


# Equation: -2x² - 9 - 35 = 0
print(solve_quadratic_equation(a=-2, b=9, c=35))  # (-2.5, 7.0)
