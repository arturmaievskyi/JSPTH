from abc import ABC, abstractmethod 

class Console(ABC):


    def log(arguments):
        print(arguments)

    def Write(arguments):
        Console.log(arguments)

    def WrtiteLine(arguments):
        '''
        The function is recomended to use with variables
        '''
        Console.log(arguments)


    def get(text):
        text_input = input(text)


    def IntGet(text):
        text_input = int(input(text))
    


    def FloatInt(text):
        text_input = float(input(text))
