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

class Convertation():
    def convert_distance(value: float, from_unit: str, to_unit: str) -> float:
        # Conversion factors to meters
        conversion_factors = {
            'miles': 1609.34,
            'kilometers': 1000.0,
            'meters': 1.0,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'yards': 0.9144,
            'feet': 0.3048,
            'inches': 0.0254
        }
        
        # Normalize unit names
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Check if units are valid
        if from_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit for 'from': {from_unit}")
        if to_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit for 'to': {to_unit}")

        # Convert 'value' to meters, then from meters to the target unit
        value_in_meters = value * conversion_factors[from_unit]
        converted_value = value_in_meters / conversion_factors[to_unit]
        
        return converted_value


    def convert_time(value: float, from_unit: str, to_unit: str) -> float:
        # Conversion factors to seconds
        conversion_factors = {
            'seconds': 1.0,
            'minutes': 60.0,
            'hours': 3600.0,
            'days': 86400.0,
            'weeks': 604800.0
        }
        
        # Normalize unit names
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Check if units are valid
        if from_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit for 'from': {from_unit}")
        if to_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit for 'to': {to_unit}")

        # Convert 'value' to seconds, then from seconds to the target unit
        value_in_seconds = value * conversion_factors[from_unit]
        converted_value = value_in_seconds / conversion_factors[to_unit]
        
        return converted_value
    
class StorageConverter:
    # Conversion factors for storage units in bytes (binary system)
    units_in_bytes = {
        'bytes': 1,
        'kilobytes': 1024,
        'megabytes': 1024 ** 2,
        'gigabytes': 1024 ** 3,
        'terabytes': 1024 ** 4,
        'petabytes': 1024 ** 5,
        'exabytes': 1024 ** 6
    }

    @staticmethod
    def convert_storage(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a storage value from one unit to another.
        """
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Check if units are valid
        if from_unit not in StorageConverter.units_in_bytes:
            raise ValueError(f"Unsupported 'from' unit: {from_unit}")
        if to_unit not in StorageConverter.units_in_bytes:
            raise ValueError(f"Unsupported 'to' unit: {to_unit}")

        # Convert the input value to bytes, then to the target unit
        value_in_bytes = value * StorageConverter.units_in_bytes[from_unit]
        converted_value = value_in_bytes / StorageConverter.units_in_bytes[to_unit]
        
        return converted_value

    @staticmethod
    def format_storage(size_in_bytes: float) -> str:
        """
        Format a byte size into a readable string (e.g., '10.5 MB').
        """
        for unit in ['bytes', 'kilobytes', 'megabytes', 'gigabytes', 'terabytes', 'petabytes', 'exabytes']:
            if size_in_bytes < StorageConverter.units_in_bytes[unit] * 1024 or unit == 'exabytes':
                formatted_size = size_in_bytes / StorageConverter.units_in_bytes[unit]
                return f"{formatted_size:.2f} {unit.capitalize()}"
        return f"{size_in_bytes:.2f} Bytes"

    @staticmethod
    def data_transfer_time(file_size: float, file_unit: str, bandwidth: float, bandwidth_unit: str) -> float:
        """
        Calculate the time required to transfer a file given a certain bandwidth.
        
        :param file_size: Size of the file to transfer.
        :param file_unit: Unit of file size (e.g., 'megabytes', 'gigabytes').
        :param bandwidth: Transfer rate (e.g., 100 for 100 Mbps).
        :param bandwidth_unit: Bandwidth unit (e.g., 'mbps' for megabits per second).
        :return: Time in seconds required to transfer the file.
        """
        # Conversion factors for bandwidth (convert to bits per second)
        bandwidth_units_in_bps = {
            'bps': 1,
            'kbps': 10**3,
            'mbps': 10**6,
            'gbps': 10**9,
        }
        
        # Validate units
        file_unit = file_unit.lower()
        bandwidth_unit = bandwidth_unit.lower()
        if file_unit not in StorageConverter.units_in_bytes:
            raise ValueError(f"Unsupported file unit: {file_unit}")
        if bandwidth_unit not in bandwidth_units_in_bps:
            raise ValueError(f"Unsupported bandwidth unit: {bandwidth_unit}")

        # Convert file size to bits and bandwidth to bits per second
        file_size_in_bits = StorageConverter.convert_storage(file_size, file_unit, 'bytes') * 8
        bandwidth_in_bps = bandwidth * bandwidth_units_in_bps[bandwidth_unit]
        
        # Calculate time in seconds
        transfer_time_seconds = file_size_in_bits / bandwidth_in_bps
        return transfer_time_seconds

    @staticmethod
    def storage_needed_for_duration(bitrate: float, bitrate_unit: str, duration_seconds: int) -> float:
        """
        Calculate the required storage for a specific duration at a given bitrate.
        
        :param bitrate: Data rate (e.g., 5 for 5 Mbps).
        :param bitrate_unit: Unit of bitrate (e.g., 'mbps').
        :param duration_seconds: Duration in seconds.
        :return: Required storage in bytes.
        """
        # Conversion factors for bitrate (convert to bits per second)
        bitrate_units_in_bps = {
            'bps': 1,
            'kbps': 10**3,
            'mbps': 10**6,
            'gbps': 10**9,
        }
        
        # Validate bitrate unit
        bitrate_unit = bitrate_unit.lower()
        if bitrate_unit not in bitrate_units_in_bps:
            raise ValueError(f"Unsupported bitrate unit: {bitrate_unit}")

        # Convert bitrate to bits per second and calculate total storage needed
        bitrate_in_bps = bitrate * bitrate_units_in_bps[bitrate_unit]
        total_bits = bitrate_in_bps * duration_seconds
        total_bytes = total_bits / 8  # Convert bits to bytes

        return total_bytes
