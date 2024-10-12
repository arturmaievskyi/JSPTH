from abc import ABC, abstractmethod 
from sys import*

class Console(ABC):


    def log(arguments):
        print(arguments)

    def __init__(self) -> None:
        super().__init__()

    def Wrtite(arguments):
        Console.log(arguments)

    def WrtiteLine(arguments):
        Console.log(arguments)


    def get(text):
        input(text)

    def IntGet(text):
        int(input(text))

    def FloatInt(text):
        float(input(text))
    
