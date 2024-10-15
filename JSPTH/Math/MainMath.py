from abc import ABC, abstractmethod
import cmath



class MyMath(ABC):
    def square_number(num: int) -> int:
        print(num**2)

    def root(num: float) -> complex:
        print(cmath.sqrt(num))

    def subtract_numbers(num1: int, num2: int) -> int:
        print(num1 - num2)

    def add(num_one: int, num_two: int) -> int:
        num = int(num_one + num_two)
        print(num)


    def divide_numbers(num1: int, num2: int) -> int:
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        print(num1 / num2)

    def multiply(num1: int, num2: int) -> int:
        num_3 = num1*num2
        print(num_3)


    # def factorial(n: int) -> int:
    #     """
    #     Calculate the factorial of a given number using a loop.

    #     Parameters:
    #     n (int): The number to calculate the factorial for.

    #     Returns:
    #     int: The factorial of the number.

    #     Raises:
    #     ValueError: If the number is negative.
    #     """
    #     if n < 0:
    #         raise ValueError("Factorial is not defined for negative numbers.")
    #     elif n == 0 or n == 1:
    #         return 1
    #     else:
    #         result = 1
    #         for i in range(2, n + 1):
    #             result *= i
    #     print(result)
