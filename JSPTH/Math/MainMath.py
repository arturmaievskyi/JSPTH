'''
Please dont forget to make a variable when dou are going to 



'''
from abc import ABC, abstractmethod
import cmath



class MyMath(ABC):
    def square_number(num: int) -> int:
        squard_num = num**2
        return(squard_num)

    def root(num: float) -> complex:
        rooted_num = (cmath.sqrt(num))
        return rooted_num
    

    
    def subtract_numbers(num1: int, num2: int) -> int:
        subtracted_num = (num1 - num2)
        return subtracted_num

    def add(num_one: int, num_two: int) -> int:
        num = int(num_one + num_two)
        return(num)


    def divide_numbers(num1: int, num2: int) -> int:
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        divided_num = (num1 / num2)
        return divided_num
    

    
    def multiply(num1: int, num2: int) -> int:
        num_3 = num1*num2
        return(num_3)


    def factorial(n: int) -> int:
        """
        Calculate the factorial of a given number using a loop.

        Parameters:
        n (int): The number to calculate the factorial for.

        Returns:
        int: The factorial of the number.

        Raises:
        ValueError: If the number is negative.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
        return(result)