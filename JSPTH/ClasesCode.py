from abc import ABC, abstractmethod 

class Console(ABC):


    def log(arguments):
        print(arguments)

    def Write(arguments):
        Console.log(arguments)

    def WrtiteLine(arguments):
        Console.log(arguments)


    def get(text):
        text_input = input(text)
        return text_input


    def IntGet(text):
        text_input = int(input(text))
        return text_input
    


    def FloatInt(text):
        text_input = float(input(text))
        return text_input
