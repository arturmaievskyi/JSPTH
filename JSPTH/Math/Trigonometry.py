import math


class Trigonometry():
    def sine(angle_in_degrees: float) -> float:
        """
        Calculate the sine of an angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The sine of the angle.
        """
        sine_answ =  math.sin(math.radians(angle_in_degrees))
        return sine_answ
    


    
    def cosine(angle_in_degrees: float) -> float:
        """
        Calculate the cosine of an angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The cosine of the angle.
        """
        cosine_answ =  math.cos(math.radians(angle_in_degrees))
        return cosine_answ
    



    def tangent(angle_in_degrees: float) -> float:
        """
        Calculate the tangent of an angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The tangent of the angle.
        """
        tan_answ =  math.tan(math.radians(angle_in_degrees))
        return tan_answ
    


    def arcsine(value: float) -> float:
        """
        Calculate the arcsine (inverse sine) of a value.
        
        Parameters:
        value (float): The value for which to calculate the arcsine.
        
        Returns:
        float: The arcsine of the value, in degrees.
        
        Raises:
        ValueError: If the value is not in the range [-1, 1].
        """
        if value < -1 or value > 1:
            raise ValueError("Input value for arcsine must be in the range [-1, 1]")
        arcsine_answ =  math.degrees(math.asin(value))
        return arcsine_answ

    def arccosine(value: float) -> float:
        """
        Calculate the arccosine (inverse cosine) of a value.
        
        Parameters:
        value (float): The value for which to calculate the arccosine.
        
        Returns:
        float: The arccosine of the value, in degrees.
        
        Raises:
        ValueError: If the value is not in the range [-1, 1].
        """
        if value < -1 or value > 1:
            raise ValueError("Input value for arccosine must be in the range [-1, 1]")
        arcosine_answ =  math.degrees(math.acos(value))
        return arcosine_answ

    def arctangent(value: float) -> float:
        """
        Calculate the arctangent (inverse tangent) of a value.
        
        Parameters:
        value (float): The value for which to calculate the arctangent.
        
        Returns:
        float: The arctangent of the value, in degrees.
        """
        arctagent_answ = math.degrees(math.atan(value))
        return arctagent_answ

    def law_of_cosines(a: float, b: float, angle_in_degrees: float) -> float:
        """
        Calculate the length of the third side of a triangle using the Law of Cosines.
        
        Parameters:
        a (float): Length of the first side.
        b (float): Length of the second side.
        angle_in_degrees (float): The angle between the two sides, in degrees.
        
        Returns:
        float: The length of the third side.
        """
        angle_in_radians = math.radians(angle_in_degrees)
        return math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_in_radians))
    
    def law_of_sines(a: float, A_in_degrees: float, B_in_degrees: float) -> float:
        """
        Calculate the length of the second side of a triangle using the Law of Sines.
        
        Parameters:
        a (float): The length of the first side.
        A_in_degrees (float): The angle opposite side 'a', in degrees.
        B_in_degrees (float): The angle opposite the side you are trying to find, in degrees.
        
        Returns:
        float: The length of the side opposite angle B.
        """
        A_in_radians = math.radians(A_in_degrees)
        B_in_radians = math.radians(B_in_degrees)
        return (a / math.sin(A_in_radians)) * math.sin(B_in_radians)
    

    def secant(angle_in_degrees: float) -> float:
        """
        Calculate the secant of an angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The secant of the angle.
        
        Raises:
        ValueError: If the cosine of the angle is zero, secant is undefined.
        """
        cos_value = math.cos(math.radians(angle_in_degrees))
        if cos_value == 0:
            raise ValueError("Secant is undefined for this angle because cosine is zero.")
        return 1 / cos_value

    def cosecant(angle_in_degrees: float) -> float:
        """
        Calculate the cosecant of an angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The cosecant of the angle.
        
        Raises:
        ValueError: If the sine of the angle is zero, cosecant is undefined.
        """
        sin_value = math.sin(math.radians(angle_in_degrees))
        if sin_value == 0:
            raise ValueError("Cosecant is undefined for this angle because sine is zero.")
        return 1 / sin_value

    def cotangent(angle_in_degrees: float) -> float:
        """
        Calculate the cotangent of an angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The cotangent of the angle.
        
        Raises:
        ValueError: If the tangent of the angle is zero, cotangent is undefined.
        """
        tan_value = math.tan(math.radians(angle_in_degrees))
        if tan_value == 0:
            raise ValueError("Cotangent is undefined for this angle because tangent is zero.")
        return 1 / tan_value

    def sine_sum(angle_a_degrees: float, angle_b_degrees: float) -> float:
        """
        Calculate the sine of the sum of two angles (in degrees).
        
        Parameters:
        angle_a_degrees (float): The first angle in degrees.
        angle_b_degrees (float): The second angle in degrees.
        
        Returns:
        float: The sine of the sum of the two angles.
        """
        angle_a_radians = math.radians(angle_a_degrees)
        angle_b_radians = math.radians(angle_b_degrees)
        return math.sin(angle_a_radians) * math.cos(angle_b_radians) + math.cos(angle_a_radians) * math.sin(angle_b_radians)

    def cosine_sum(angle_a_degrees: float, angle_b_degrees: float) -> float:
        """
        Calculate the cosine of the sum of two angles (in degrees).
        
        Parameters:
        angle_a_degrees (float): The first angle in degrees.
        angle_b_degrees (float): The second angle in degrees.
        
        Returns:
        float: The cosine of the sum of the two angles.
        """
        angle_a_radians = math.radians(angle_a_degrees)
        angle_b_radians = math.radians(angle_b_degrees)
        return math.cos(angle_a_radians) * math.cos(angle_b_radians) - math.sin(angle_a_radians) * math.sin(angle_b_radians)

    def tangent_sum(angle_a_degrees: float, angle_b_degrees: float) -> float:
        """
        Calculate the tangent of the sum of two angles (in degrees).
        
        Parameters:
        angle_a_degrees (float): The first angle in degrees.
        angle_b_degrees (float): The second angle in degrees.
        
        Returns:
        float: The tangent of the sum of the two angles.
        
        Raises:
        ValueError: If the denominator is zero, the tangent is undefined.
        """
        angle_a_radians = math.radians(angle_a_degrees)
        angle_b_radians = math.radians(angle_b_degrees)
        denominator = 1 - math.tan(angle_a_radians) * math.tan(angle_b_radians)
        if denominator == 0:
            raise ValueError("Tangent of the sum is undefined for this angle.")
        return (math.tan(angle_a_radians) + math.tan(angle_b_radians)) / denominator



    def sine_double(angle_in_degrees: float) -> float:
        """
        Calculate the sine of a double angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The sine of the double angle.
        """
        angle_in_radians = math.radians(angle_in_degrees)
        return 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)


    def cosine_double(angle_in_degrees: float) -> float:
        """
        Calculate the cosine of a double angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The cosine of the double angle.
        """
        angle_in_radians = math.radians(angle_in_degrees)
        return math.cos(angle_in_radians)**2 - math.sin(angle_in_radians)**2

    def tangent_double(angle_in_degrees: float) -> float:
        """
        Calculate the tangent of a double angle (in degrees).
        
        Parameters:
        angle_in_degrees (float): The angle in degrees.
        
        Returns:
        float: The tangent of the double angle.
        
        Raises:
        ValueError: If the denominator is zero, the tangent is undefined.
        """
        angle_in_radians = math.radians(angle_in_degrees)
        denominator = 1 - math.tan(angle_in_radians)**2
        if denominator == 0:
            raise ValueError("Tangent of the double angle is undefined for this angle.")
        return (2 * math.tan(angle_in_radians)) / denominator


    def polar_to_cartesian(r: float, theta_in_degrees: float) -> tuple:
        """
        Convert polar coordinates to Cartesian coordinates.
        
        Parameters:
        r (float): The radius.
        theta_in_degrees (float): The angle in degrees.
        
        Returns:
        tuple: A tuple containing the Cartesian coordinates (x, y).
        """
        theta_in_radians = math.radians(theta_in_degrees)
        x = r * math.cos(theta_in_radians)
        y = r * math.sin(theta_in_radians)
        return (x, y)



    def cartesian_to_polar(x: float, y: float) -> tuple:
        """
        Convert Cartesian coordinates to polar coordinates.
        
        Parameters:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
        
        Returns:
        tuple: A tuple containing the polar coordinates (r, theta) where
            r is the radius and theta is the angle in degrees.
        """
        r = math.sqrt(x**2 + y**2)
        theta = math.degrees(math.atan2(y, x))
        return (r, theta)
