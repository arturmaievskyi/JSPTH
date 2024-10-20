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
        return math.degrees(math.acos(value))
    

    def arctangent(value: float) -> float:
        """
        Calculate the arctangent (inverse tangent) of a value.
        
        Parameters:
        value (float): The value for which to calculate the arctangent.
        
        Returns:
        float: The arctangent of the value, in degrees.
        """
        return math.degrees(math.atan(value))


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

