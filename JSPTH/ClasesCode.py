from abc import ABC, abstractmethod 
import asyncio
from pathlib import Path
import os
import threading
import time
import subprocess
import shutil
import hashlib
import hmac




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
    
    def read_file_in_chunks(file_path: str, chunk_size: int = 1024):
        """Reads a file in chunks."""
        with open(file_path, 'r') as file:
            while chunk := file.read(chunk_size):
                yield chunk




class EventEmitter:
    def __init__(self):
        self._events = {}

    def on(self, event, listener):
        """Registers an event listener (similar to 'on' in Node.js)."""
        if event not in self._events:
            self._events[event] = []
        self._events[event].append(listener)

    def once(self, event, listener):
        """Registers a one-time listener (executes once and then removes itself)."""
        def one_time_listener(*args, **kwargs):
            listener(*args, **kwargs)
            self.off(event, one_time_listener)
        self.on(event, one_time_listener)

    def off(self, event, listener=None):
        """Removes a specific listener or all listeners for an event (similar to 'off')."""
        if listener:
            if event in self._events:
                self._events[event] = [l for l in self._events[event] if l != listener]
        else:
            if event in self._events:
                del self._events[event]

    def remove_all_listeners(self, event=None):
        """Removes all listeners for a specific event or all events."""
        if event:
            if event in self._events:
                del self._events[event]
        else:
            self._events.clear()

    def emit(self, event, *args, **kwargs):
        """Emits an event (similar to 'emit' in Node.js)."""
        if event in self._events:
            for listener in self._events[event]:
                listener(*args, **kwargs)





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
    

