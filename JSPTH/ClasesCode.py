from abc import ABC, abstractmethod 
import asyncio
from pathlib import Path
import os
import threading
import time
import subprocess
import shutil
import subprocess
import signal
import sys
from setproctitle import setproctitle
from multiprocessing import Process, Pipe, Queue

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



class TimeManager:
    def __init__(self):
        self.timers = {}
        self.intervals = {}

    # setTimeout equivalent
    def set_timeout(self, callback, delay):
        def timeout():
            time.sleep(delay / 1000)  # Convert milliseconds to seconds
            callback()

        # Start timeout in a new thread
        thread = threading.Thread(target=timeout)
        thread.start()
        self.timers[thread.ident] = thread

    # clearTimeout equivalent
    def clear_timeout(self, timer_id):
        timer = self.timers.get(timer_id)
        if timer:
            timer.join(timeout=0)  # Stop the timer thread
            del self.timers[timer_id]

    # setInterval equivalent
    def set_interval(self, callback, interval):
        def repeat():
            while True:
                time.sleep(interval / 1000)  # Convert milliseconds to seconds
                callback()

        # Start interval in a new thread
        thread = threading.Thread(target=repeat)
        thread.daemon = True  # Daemon thread so it terminates with the program
        thread.start()
        self.intervals[thread.ident] = thread

    # clearInterval equivalent
    def clear_interval(self, interval_id):
        interval = self.intervals.get(interval_id)
        if interval:
            interval.join(timeout=0)  # Stop the interval thread
            del self.intervals[interval_id]

    # process.hrtime equivalent
    def hrtime(self, start=None):
        if start:
            # Return the difference between the current time and the start time
            end = time.perf_counter_ns()
            return end - start
        else:
            # Return current high-resolution time
            return time.perf_counter_ns()


class ProcessManager:
    
    def __init__(self):
        print("Process Manager Initialized")

    # Method to get the current process ID
    def get_pid(self):
        return os.getpid()

    # Method to get the current working directory
    def get_cwd(self):
        return os.getcwd()

    # Method to get environment variables
    def get_env_vars(self):
        return os.environ

    # Method to get a specific environment variable
    def get_env_var(self, var_name):
        return os.environ.get(var_name)

    # Method to spawn a process (equivalent to Node's `spawn`)
    def spawn_process(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stdout:
            print(f'stdout: {stdout.decode()}')
        if stderr:
            print(f'stderr: {stderr.decode()}')

        return process.returncode

    # Method to execute a command (equivalent to Node's `exec`)
    def execute_command(self, command):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            print(f'stdout: {result.stdout}')
            if result.stderr:
                print(f'stderr: {result.stderr}')
        except subprocess.CalledProcessError as e:
            print(f'Execution failed: {e}')

    # Method to handle signals (equivalent to `process.on`)
    def handle_signal(self, sig, handler):
        signal.signal(sig, handler)

    # Method to exit the process (equivalent to `process.exit`)
    def exit_process(self, code=0):
        sys.exit(code)

    # Method to fork a process (equivalent to `child_process.fork`)
    def fork_process(self, target_func):
        parent_conn, child_conn = Pipe()
        process = Process(target=target_func, args=(child_conn,))
        process.start()
        message = parent_conn.recv()
        process.join()
        return message

    # Example target function for forking
    @staticmethod
    def child_process_example(conn):
        conn.send('Hello from child process')
        conn.close()

    # Method to set process title (requires `setproctitle` package)
    def set_process_title(self, title):
        try:
            
            setproctitle(title)
            print(f'Process title set to: {title}')
        except ImportError:
            print("setproctitle module is not installed. Please install it to use this functionality.")

