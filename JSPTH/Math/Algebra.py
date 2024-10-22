import math



class Algebra():
    pass



def quadratic_solver(a: float, b: float, c: float) -> tuple:
    """
    Solves the quadratic equation ax^2 + bx + c = 0 using the quadratic formula.
    
    Parameters:
    a (float): Coefficient of x^2.
    b (float): Coefficient of x.
    c (float): Constant term.
    
    Returns:
    tuple: Two solutions of the quadratic equation.
    
    Raises:
    ValueError: If the equation has no real solutions.
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("This equation has no real solutions.")
    
    sol1 = (-b + math.sqrt(discriminant)) / (2 * a)
    sol2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    return sol1, sol2



def linear_solver(a: float, b: float) -> float:
    """
    Solves the linear equation ax + b = 0.
    
    Parameters:
    a (float): Coefficient of x.
    b (float): Constant term.
    
    Returns:
    float: The solution of the linear equation.
    
    Raises:
    ValueError: If a is zero (which would not be a valid equation).
    """
    if a == 0:
        raise ValueError("The equation is invalid (a cannot be zero).")
    
    return -b / a


def exponential_solver(a: float, b: float) -> float:
    """
    Solves the exponential equation a^x = b.
    
    Parameters:
    a (float): The base.
    b (float): The result.
    
    Returns:
    float: The value of x.
    
    Raises:
    ValueError: If the equation is invalid.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Base and result must be positive.")
    
    return math.log(b) / math.log(a)



def logarithm_solver(a: float, b: float) -> float:
    """
    Solves the logarithmic equation log_a(b).
    
    Parameters:
    a (float): The base of the logarithm.
    b (float): The result of the logarithm.
    
    Returns:
    float: The value of log_a(b).
    
    Raises:
    ValueError: If the base or result is not valid.
    """
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Base and result must be positive and base cannot be 1.")
    
    return math.log(b) / math.log(a)
