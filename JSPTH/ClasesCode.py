from abc import ABC, abstractmethod 
import asyncio
from pathlib import Path
import os
import threading
import time
import subprocess
import shutil




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
    

class FunctionsAndFiles(ABC):
    @abstractmethod
    async def async_task(name: str, delay: int, text: float):
        print(f"{float}{name}")
        await asyncio.sleep(delay)
        print(f"Task {name} finished after {delay} seconds")

    async def read_file(file_path: str) -> str:
        """Reads the contents of a file."""
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(file_path: str, content: str) -> None:
        """Writes content to a file."""
        with open(file_path, 'w') as file:
            file.write(content)

    def copy_file(source: str, destination: str) -> None:
        """Copies a file from source to destination."""
        shutil.copy(source, destination)


    def get_basename(file_path: str) -> str:
        """Returns the base name of a file."""
        return Path(file_path).name

    def get_extension(file_path: str) -> str:
        """Returns the file extension."""
        return Path(file_path).suffix

    def join_paths(*paths) -> str:
        """Joins multiple paths together."""
        return str(Path(*paths))


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

class Managment(ABC):
    def string_to_bytes(data: str) -> bytes:
        """Converts a string to bytes."""
        return data.encode('utf-8')

    def bytes_to_string(data: bytes) -> str:
        """Converts bytes to a string."""
        return data.decode('utf-8')
    def get_full_path(*paths) -> str:
        """Combines and resolves paths."""
        return str(Path(*paths).resolve())
    
    def get_env_variable(var_name: str) -> str:
        return os.getenv(var_name)
    
    def create_buffer(size: int) -> bytearray:
        """Creates a buffer of a specified size."""
        return bytearray(size)

    def write_to_buffer(buffer: bytearray, data: str, offset: int = 0):
        """Writes data to a buffer at a specific offset."""
        buffer[offset:offset+len(data)] = data.encode()

    def read_from_buffer(buffer: bytearray, start: int = 0, end: int = None) -> str:
        """Reads data from a buffer from start to end."""
        if end is None:
            end = len(buffer)
        return buffer[start:end].decode()



class Timer:
    def set_timeout(callback, delay: int):
        """Runs a callback function after a delay."""
        timer = threading.Timer(delay, callback)
        timer.start()
        return timer
    
    def set_interval(callback, interval: int):
        """Runs a callback repeatedly at a specified interval."""
        def loop():
            while True:
                time.sleep(interval)
                callback()

        thread = threading.Thread(target=loop)
        thread.start()
        return thread



class ProccesorManagmet():
    def exec_command(command: str) -> str:
        """Executes a shell command and returns the output."""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout