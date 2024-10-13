from abc import ABC, abstractmethod



class Math(ABC):
    def square_number(num: int) -> int:
        print(num**2)

    def root(root_num: int, num: int) -> int:
        pass

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

