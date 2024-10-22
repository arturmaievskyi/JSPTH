from abc import ABC, abstractmethod 
import asyncio
from pathlib import Path


class Console(ABC):


    def log(arguments):
        '''
        its like print()
        '''
        print(arguments)

    def Write(arguments):
        '''
        
        '''
        Console.log(arguments)

    def WrtiteLine(arguments):
        '''
        The function is recomended to use with variables
        '''
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
    

class Functions(ABC):
    @abstractmethod
    async def async_task(name: str, delay: int, text: float):
        print(f"{float}{name}")
        await asyncio.sleep(delay)
        print(f"Task {name} finished after {delay} seconds")

    def read_file(file_path: str) -> str:
        """Reads the contents of a file."""
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(file_path: str, content: str) -> None:
        """Writes content to a file."""
        with open(file_path, 'w') as file:
            file.write(content)


class EventEmitter:
    def __init__(self):
        self.events = {}

    def on(self, event: str, callback):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(callback)

    def emit(self, event: str, *args, **kwargs):
        if event in self.events:
            for callback in self.events[event]:
                callback(*args, **kwargs)

# Example usage
emitter = EventEmitter()
emitter.on('greet', lambda name: print(f"Hello, {name}!"))
emitter.emit('greet', 'Alice')


class Managment(ABC):
    def string_to_bytes(data: str) -> bytes:
        """Converts a string to bytes."""
        return data.encode('utf-8')

    def bytes_to_string(data: bytes) -> str:
        """Converts bytes to a string."""
        return data.decode('utf-8')
