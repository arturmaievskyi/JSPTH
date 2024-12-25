from abc import ABC, abstractmethod 
# import asyncio
from pathlib import Path
import os
import threading
import time
import shutil
import subprocess
import signal
import sys
from setproctitle import setproctitle
from multiprocessing import Process, Pipe
import psutil
import platform
import math
import time
import hashlib
import hmac
from functools import wraps
import csv
import json
import gzip
import sqlite3
from crontab import CronTab
import time
import requests
from typing import Dict, Optional, List, Any, Optional
import locale
from babel import dates, numbers
from faker import Faker
import datetime
import pymysql
import pg8000

class UtilityClass(ABC):
    """
    A unified utility class with various decorators and cryptographic/hashing functionality.
    """

    # ------------------------
    # Logging Decorator
    # ------------------------

    @staticmethod
    def log_execution(func):
        """
        Logs the function name, arguments, and return value.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Executing {func.__name__} with args={args} kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return wrapper

    # ------------------------
    # Access Control Decorator
    # ------------------------

    @staticmethod
    def require_role(role):
        """
        Enforces access control by checking user role.
        """
        def decorator(func):
            @wraps(func)
            def wrapper(user, *args, **kwargs):
                if user.get("role") != role:
                    raise PermissionError(f"User does not have the required role: {role}")
                return func(user, *args, **kwargs)
            return wrapper
        return decorator

    # ------------------------
    # Caching Decorator
    # ------------------------

    @staticmethod
    def cache_results(func):
        """
        Caches the results of the function based on its arguments.
        """
        cache = {}

        @wraps(func)
        def wrapper(*args):
            if args in cache:
                print(f"Cache hit for args={args}")
                return cache[args]
            print(f"Cache miss for args={args}")
            result = func(*args)
            cache[args] = result
            return result
        return wrapper

    # ------------------------
    # Validation Decorator
    # ------------------------

    @staticmethod
    def validate_positive(func):
        """
        Ensures all arguments are positive numbers.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            if any(arg < 0 for arg in args if isinstance(arg, (int, float))):
                raise ValueError("All arguments must be positive.")
            return func(*args, **kwargs)
        return wrapper

    # ------------------------
    # Retry Decorator
    # ------------------------

    @staticmethod
    def retry(times=3, delay=1):
        """
        Retries the function a specified number of times with a delay.
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                attempts = 0
                while attempts < times:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(f"Attempt {attempts + 1} failed: {e}")
                        attempts += 1
                        time.sleep(delay)
                raise RuntimeError(f"Function {func.__name__} failed after {times} attempts")
            return wrapper
        return decorator

    # ------------------------
    # Execution Time Decorator
    # ------------------------

    @staticmethod
    def measure_time(func):
        """
        Measures the execution time of the function.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper

class console(ABC):
    def log(arguments):
        '''
        its like print()
        '''
        print(arguments)

    def Write(arguments):
        '''
        
        '''
        console.log(arguments)

    def WrtiteLine(arguments):
        '''
        The function is recomended to use with variables
        '''
        console.log(arguments)


    def Get(text):
        text_input = input(text)
        return text_input


    def IntGet(text):
        text_input = int(input(text))
        return text_input


    def FloatGet(text):
        text_input = float(input(text))
        return text_input
  
class Files(ABC):

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

class AreaConverter:
    # Conversion factors for area units (square meters as base unit)
    units_in_square_meters = {
        'square_meters': 1,
        'square_kilometers': 1e6,
        'square_centimeters': 1e-4,
        'square_millimeters': 1e-6,
        'square_inches': 0.00064516,
        'square_feet': 0.092903,
        'square_yards': 0.836127,
        'acres': 4046.8564224,
        'hectares': 10000
    }

    @staticmethod
    def convert_area(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert an area value from one unit to another.
        
        :param value: Numeric area value to convert.
        :param from_unit: Unit of the input area (e.g., "square_meters", "acres").
        :param to_unit: Target unit to convert to (e.g., "square_kilometers").
        :return: Converted area value.
        """
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Check if units are valid
        if from_unit not in AreaConverter.units_in_square_meters:
            raise ValueError(f"Unsupported 'from' unit: {from_unit}")
        if to_unit not in AreaConverter.units_in_square_meters:
            raise ValueError(f"Unsupported 'to' unit: {to_unit}")

        # Convert the value to square meters, then to the target unit
        value_in_square_meters = value * AreaConverter.units_in_square_meters[from_unit]
        converted_value = value_in_square_meters / AreaConverter.units_in_square_meters[to_unit]
        
        return converted_value

    @staticmethod
    def format_area(size_in_square_meters: float) -> str:
        """
        Format an area size into a readable string (e.g., '10.5 square meters').
        
        :param size_in_square_meters: Area size in square meters.
        :return: Readable formatted string.
        """
        for unit, factor in AreaConverter.units_in_square_meters.items():
            if size_in_square_meters < factor * 1000 or unit == 'hectares':
                formatted_size = size_in_square_meters / factor
                return f"{formatted_size:.2f} {unit.replace('_', ' ').capitalize()}"
        return f"{size_in_square_meters:.2f} Square meters"

    @staticmethod
    def area_of_rectangle(length: float, width: float, unit: str = "square_meters") -> float:
        """
        Calculate the area of a rectangle.
        
        :param length: Length of the rectangle.
        :param width: Width of the rectangle.
        :param unit: Desired output unit (default is 'square_meters').
        :return: Area of the rectangle in the specified unit.
        """
        area_in_square_meters = length * width
        return AreaConverter.convert_area(area_in_square_meters, 'square_meters', unit)

    @staticmethod
    def area_of_circle(radius: float, unit: str = "square_meters") -> float:
        """
        Calculate the area of a circle.
        
        :param radius: Radius of the circle.
        :param unit: Desired output unit (default is 'square_meters').
        :return: Area of the circle in the specified unit.
        """
        area_in_square_meters = 3.14159 * (radius ** 2)
        return AreaConverter.convert_area(area_in_square_meters, 'square_meters', unit)

    @staticmethod
    def area_of_triangle(base: float, height: float, unit: str = "square_meters") -> float:
        """
        Calculate the area of a triangle.
        
        :param base: Base length of the triangle.
        :param height: Height of the triangle.
        :param unit: Desired output unit (default is 'square_meters').
        :return: Area of the triangle in the specified unit.
        """
        area_in_square_meters = 0.5 * base * height
        return AreaConverter.convert_area(area_in_square_meters, 'square_meters', unit)

class VolumeConverter:
    # Conversion factors for volume units (liters as base unit)
    units_in_liters = {
        'liters': 1,
        'milliliters': 1e-3,
        'cubic_meters': 1e3,
        'cubic_centimeters': 1e-3,
        'cubic_inches': 0.0163871,
        'cubic_feet': 28.3168,
        'cubic_yards': 764.555,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'fluid_ounces': 0.0295735
    }

    @staticmethod
    def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a volume value from one unit to another.
        
        :param value: Numeric volume value to convert.
        :param from_unit: Unit of the input volume (e.g., "liters", "gallons").
        :param to_unit: Target unit to convert to (e.g., "cubic meters").
        :return: Converted volume value.
        """
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Check if units are valid
        if from_unit not in VolumeConverter.units_in_liters:
            raise ValueError(f"Unsupported 'from' unit: {from_unit}")
        if to_unit not in VolumeConverter.units_in_liters:
            raise ValueError(f"Unsupported 'to' unit: {to_unit}")

        # Convert the value to liters, then to the target unit
        value_in_liters = value * VolumeConverter.units_in_liters[from_unit]
        converted_value = value_in_liters / VolumeConverter.units_in_liters[to_unit]
        
        return converted_value

    @staticmethod
    def format_volume(size_in_liters: float) -> str:
        """
        Format a volume size into a readable string (e.g., '10.5 liters').
        
        :param size_in_liters: Volume size in liters.
        :return: Readable formatted string.
        """
        for unit, factor in VolumeConverter.units_in_liters.items():
            if size_in_liters < factor * 1000 or unit == 'cubic_meters':
                formatted_size = size_in_liters / factor
                return f"{formatted_size:.2f} {unit.replace('_', ' ').capitalize()}"
        return f"{size_in_liters:.2f} Liters"

    @staticmethod
    def volume_of_cube(side: float, unit: str = "liters") -> float:
        """
        Calculate the volume of a cube.
        
        :param side: Length of a side of the cube.
        :param unit: Desired output unit (default is 'liters').
        :return: Volume of the cube in the specified unit.
        """
        volume_in_cubic_meters = side ** 3
        return VolumeConverter.convert_volume(volume_in_cubic_meters, 'cubic_meters', unit)

    @staticmethod
    def volume_of_sphere(radius: float, unit: str = "liters") -> float:
        """
        Calculate the volume of a sphere.
        
        :param radius: Radius of the sphere.
        :param unit: Desired output unit (default is 'liters').
        :return: Volume of the sphere in the specified unit.
        """
        volume_in_cubic_meters = (4/3) * 3.14159 * (radius ** 3)
        return VolumeConverter.convert_volume(volume_in_cubic_meters, 'cubic_meters', unit)

    @staticmethod
    def volume_of_cylinder(radius: float, height: float, unit: str = "liters") -> float:
        """
        Calculate the volume of a cylinder.
        
        :param radius: Radius of the base of the cylinder.
        :param height: Height of the cylinder.
        :param unit: Desired output unit (default is 'liters').
        :return: Volume of the cylinder in the specified unit.
        """
        volume_in_cubic_meters = 3.14159 * (radius ** 2) * height
        return VolumeConverter.convert_volume(volume_in_cubic_meters, 'cubic_meters', unit)

class OSUtilities:
    @staticmethod
    def get_os_type():
        return os.name  # Returns 'posix', 'nt', etc.

    @staticmethod
    def get_platform():
        return platform.system()  # Returns 'Windows', 'Linux', 'Darwin', etc.

    @staticmethod
    def get_platform_version():
        return platform.version()  # Returns the OS version.

    @staticmethod
    def get_architecture():
        return platform.architecture()[0]  # Returns '32bit' or '64bit'.

    @staticmethod
    def get_cpus():
        return os.cpu_count()  # Returns the number of CPUs.

    @staticmethod
    def get_memory_info():
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used,
            "percent": mem.percent
        }

    @staticmethod
    def get_disk_info():
        disk = psutil.disk_usage('/')
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        }

    # @staticmethod
    # def get_boot_time():
    #     boot_time = psutil.boot_time()
    #     return platform.uname()._replace(boot_time = boot_time)

    @staticmethod
    def get_user_info():
        return psutil.users()  # Returns a list of logged-in users.

class SpeedConverter:
    # Conversion factors for speed (meters per second as the base unit)
    units_in_meters_per_second = {
        'mps': 1,  # Meters per second
        'kmph': 1 / 3.6,  # Kilometers per hour to meters per second
        'mph': 0.44704,  # Miles per hour to meters per second
        'fps': 0.3048,  # Feet per second to meters per second
        'knots': 0.514444,  # Knots to meters per second
    }

    @staticmethod
    def convert_speed(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a speed value from one unit to another.
        
        :param value: Speed value to convert.
        :param from_unit: The current unit of the speed value (e.g., 'kmph', 'mph').
        :param to_unit: The target unit to convert to (e.g., 'mps', 'knots').
        :return: The converted speed value.
        """
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Check if units are valid
        if from_unit not in SpeedConverter.units_in_meters_per_second:
            raise ValueError(f"Unsupported 'from' unit: {from_unit}")
        if to_unit not in SpeedConverter.units_in_meters_per_second:
            raise ValueError(f"Unsupported 'to' unit: {to_unit}")

        # Convert the value to meters per second
        value_in_mps = value * SpeedConverter.units_in_meters_per_second[from_unit]
        # Convert from meters per second to the target unit
        converted_value = value_in_mps / SpeedConverter.units_in_meters_per_second[to_unit]
        
        return converted_value

    @staticmethod
    def format_speed(value: float, unit: str) -> str:
        """
        Format a speed value into a readable string.
        
        :param value: Speed value to format.
        :param unit: Unit of the speed value (e.g., 'kmph', 'mph').
        :return: Formatted speed string.
        """
        return f"{value:.2f} {unit.upper()}"
    
class MassConverter:
    # Conversion factors (kilograms as the base unit)
    units_in_kilograms = {
        'kg': 1,             # Kilogram
        'g': 1e-3,           # Gram
        'mg': 1e-6,          # Milligram
        'ton': 1e3,          # Metric ton
        'lb': 0.453592,      # Pound
        'oz': 0.0283495,     # Ounce
        'stone': 6.35029,    # Stone
        'us_ton': 907.184,   # US ton
        'imperial_ton': 1016.05,  # Imperial ton
    }

    @staticmethod
    def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a mass value from one unit to another.

        :param value: Mass value to convert.
        :param from_unit: The current unit of the mass value (e.g., 'kg', 'lb').
        :param to_unit: The target unit to convert to (e.g., 'g', 'oz').
        :return: The converted mass value.
        """
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Check if units are valid
        if from_unit not in MassConverter.units_in_kilograms:
            raise ValueError(f"Unsupported 'from' unit: {from_unit}")
        if to_unit not in MassConverter.units_in_kilograms:
            raise ValueError(f"Unsupported 'to' unit: {to_unit}")

        # Convert the value to kilograms
        value_in_kg = value * MassConverter.units_in_kilograms[from_unit]
        # Convert from kilograms to the target unit
        converted_value = value_in_kg / MassConverter.units_in_kilograms[to_unit]

        return converted_value

    @staticmethod
    def format_mass(value: float, unit: str) -> str:
        """
        Format a mass value into a readable string.

        :param value: Mass value to format.
        :param unit: Unit of the mass value (e.g., 'kg', 'lb').
        :return: Formatted mass string.
        """
        return f"{value:.2f} {unit.upper()}"

class DistanceConverter:
    units_in_meters = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
        'nm': 1e-9
    }

    @staticmethod
    def convert_distance(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in DistanceConverter.units_in_meters or to_unit not in DistanceConverter.units_in_meters:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
        value_in_meters = value * DistanceConverter.units_in_meters[from_unit]
        return value_in_meters / DistanceConverter.units_in_meters[to_unit]

class TemperatureConverter:
    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit == to_unit:
            return value

        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return value * 9 / 5 + 32
            elif to_unit == 'kelvin':
                return value + 273.15

        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * 5 / 9
            elif to_unit == 'kelvin':
                return (value - 32) * 5 / 9 + 273.15

        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            elif to_unit == 'fahrenheit':
                return (value - 273.15) * 9 / 5 + 32

        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

class PressureConverter:
    units_in_pascals = {
        'pa': 1,            # Pascal
        'kpa': 1000,        # Kilopascal
       'mpa': 1e6,         # Megapascal
        'atm': 101325,      # Atmosphere
        'bar': 100000,      # Bar
        'psi': 6894.76,     # Pounds per square inch
        'torr': 133.322     # Torr
    }
 
    @staticmethod
    def convert_pressure(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in PressureConverter.units_in_pascals or to_unit not in PressureConverter.units_in_pascals:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_pascals = value * PressureConverter.units_in_pascals[from_unit]
        return value_in_pascals / PressureConverter.units_in_pascals[to_unit]

class EnergyConverter:
    units_in_joules = {
        'j': 1,            # Joule
        'kj': 1000,        # Kilojoule
        'cal': 4.184,      # Calorie
        'kcal': 4184,      # Kilocalorie
        'wh': 3600,        # Watt-hour
        'kwh': 3.6e6,      # Kilowatt-hour
        'btu': 1055.06     # British Thermal Unit
    }

    @staticmethod
    def convert_energy(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in EnergyConverter.units_in_joules or to_unit not in EnergyConverter.units_in_joules:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_joules = value * EnergyConverter.units_in_joules[from_unit]
        return value_in_joules / EnergyConverter.units_in_joules[to_unit]

class FrequencyConverter:
    units_in_hertz = {
        'hz': 1,           # Hertz
        'khz': 1e3,        # Kilohertz
        'mhz': 1e6,        # Megahertz
        'ghz': 1e9         # Gigahertz
    }

    @staticmethod
    def convert_frequency(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in FrequencyConverter.units_in_hertz or to_unit not in FrequencyConverter.units_in_hertz:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_hz = value * FrequencyConverter.units_in_hertz[from_unit]
        return value_in_hz / FrequencyConverter.units_in_hertz[to_unit]

class PowerConverter:
    units_in_watts = {
        'w': 1,            # Watt
        'kw': 1000,        # Kilowatt
        'mw': 1e6,         # Megawatt
        'hp': 745.7        # Horsepower
    }

    @staticmethod
    def convert_power(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in PowerConverter.units_in_watts or to_unit not in PowerConverter.units_in_watts:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_watts = value * PowerConverter.units_in_watts[from_unit]
        return value_in_watts / PowerConverter.units_in_watts[to_unit]

class ForceConverter:
    units_in_newtons = {
        'n': 1,               # Newton
        'dyne': 1e-5,         # Dyne
        'lbf': 4.44822,       # Pound-force
        'kgf': 9.80665,       # Kilogram-force
    }

    @staticmethod
    def convert_force(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in ForceConverter.units_in_newtons or to_unit not in ForceConverter.units_in_newtons:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_newtons = value * ForceConverter.units_in_newtons[from_unit]
        return value_in_newtons / ForceConverter.units_in_newtons[to_unit]

class TorqueConverter:
    units_in_newton_meter = {
        'nm': 1,               # Newton-meter
        'lbft': 1.35582,       # Pound-foot
        'kgfm': 9.80665,       # Kilogram-force meter
    }

    @staticmethod
    def convert_torque(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in TorqueConverter.units_in_newton_meter or to_unit not in TorqueConverter.units_in_newton_meter:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_nm = value * TorqueConverter.units_in_newton_meter[from_unit]
        return value_in_nm / TorqueConverter.units_in_newton_meter[to_unit]

class DensityConverter:
    units_in_kg_per_cubic_meter = {
        'kgm3': 1,                 # Kilogram per cubic meter
        'gcm3': 1000,              # Gram per cubic centimeter
        'lbft3': 16.0185,          # Pound per cubic foot
        'lbgal': 119.826,          # Pound per gallon (US)
    }

    @staticmethod
    def convert_density(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in DensityConverter.units_in_kg_per_cubic_meter or to_unit not in DensityConverter.units_in_kg_per_cubic_meter:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_kgm3 = value * DensityConverter.units_in_kg_per_cubic_meter[from_unit]
        return value_in_kgm3 / DensityConverter.units_in_kg_per_cubic_meter[to_unit]

class LuminanceConverter:
    units_in_lux = {
        'lux': 1,               # Lux
        'candela': 1 / (4 * math.pi),  # Candela to lux (approx. for point source at 1m)
        'lumen': 1 / (4 * math.pi),    # Lumen to lux (approx. for point source at 1m)
    }

    @staticmethod
    def convert_luminance(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in LuminanceConverter.units_in_lux or to_unit not in LuminanceConverter.units_in_lux:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_lux = value * LuminanceConverter.units_in_lux[from_unit]
        return value_in_lux / LuminanceConverter.units_in_lux[to_unit]

class FuelEfficiencyConverter:
    @staticmethod
    def convert_fuel_efficiency(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit == to_unit:
            return value

        if from_unit == "mpg":  # Miles per gallon (US)
            if to_unit == "kmpl":  # Kilometers per liter
                return value * 0.425144
            elif to_unit == "l/100km":  # Liters per 100 kilometers
                return 235.215 / value

        elif from_unit == "kmpl":  # Kilometers per liter
            if to_unit == "mpg":
                return value * 2.35215
            elif to_unit == "l/100km":
                return 100 / value

        elif from_unit == "l/100km":  # Liters per 100 kilometers
            if to_unit == "mpg":
                return 235.215 / value
            elif to_unit == "kmpl":
                return 100 / value

        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

class RadioactivityConverter:
    units_in_becquerel = {
        'bq': 1,            # Becquerel
        'ci': 3.7e10,       # Curie
        'rd': 1e6,          # Rutherford
    }

    @staticmethod
    def convert_radioactivity(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in RadioactivityConverter.units_in_becquerel or to_unit not in RadioactivityConverter.units_in_becquerel:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_bq = value * RadioactivityConverter.units_in_becquerel[from_unit]
        return value_in_bq / RadioactivityConverter.units_in_becquerel[to_unit]

class DataTransferRateConverter:
    units_in_bps = {
        'bps': 1,            # Bits per second
        'kbps': 1e3,         # Kilobits per second
        'mbps': 1e6,         # Megabits per second
        'gbps': 1e9,         # Gigabits per second
        'tbps': 1e12,        # Terabits per second
    }

    @staticmethod
    def convert_transfer_rate(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in DataTransferRateConverter.units_in_bps or to_unit not in DataTransferRateConverter.units_in_bps:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_bps = value * DataTransferRateConverter.units_in_bps[from_unit]
        return value_in_bps / DataTransferRateConverter.units_in_bps[to_unit]

class CapacitanceConverter:
    units_in_farads = {
        'f': 1,             # Farad
        'uf': 1e-6,         # Microfarad
        'nf': 1e-9,         # Nanofarad
        'pf': 1e-12,        # Picofarad
    }

    @staticmethod
    def convert_capacitance(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in CapacitanceConverter.units_in_farads or to_unit not in CapacitanceConverter.units_in_farads:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_farads = value * CapacitanceConverter.units_in_farads[from_unit]
        return value_in_farads / CapacitanceConverter.units_in_farads[to_unit]

class IlluminationIntensityConverter:
    units_in_lux = {
        'lux': 1,               # Lux
        'lumen': 1 / (4 * math.pi),  # Lumen
        'footcandle': 10.7639,      # Foot-candle
    }

    @staticmethod
    def convert_illumination(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in IlluminationIntensityConverter.units_in_lux or to_unit not in IlluminationIntensityConverter.units_in_lux:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_lux = value * IlluminationIntensityConverter.units_in_lux[from_unit]
        return value_in_lux / IlluminationIntensityConverter.units_in_lux[to_unit]

class DatabaseManager:
    """
    SQLite Database Manager with basic query and table handling.
    """

    def __init__(self, db_path="database.db"):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the SQLite database.
        """
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
        return self.connection

    def execute_query(self, query, params=None):
        """
        Executes a SQL query with optional parameters.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        return cursor

    def fetch_all(self, query, params=None):
        """
        Executes a query and fetches all results.
        """
        cursor = self.execute_query(query, params)
        return [dict(row) for row in cursor.fetchall()]

    def fetch_one(self, query, params=None):
        """
        Executes a query and fetches one result.
        """
        cursor = self.execute_query(query, params)
        row = cursor.fetchone()
        return dict(row) if row else None

    def create_table(self, table_name, columns):
        """
        Creates a new table with the specified columns.
        """
        columns_def = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        self.execute_query(query)

    def insert(self, table_name, data):
        """
        Inserts a record into the specified table.
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(data.values()))

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

class FileStorageManager:
    """
    File Storage Manager for handling file operations.
    """

    @staticmethod
    def write_json(file_path, data):
        """
        Writes data to a JSON file.
        """
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def read_json(file_path):
        """
        Reads data from a JSON file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found")
        with open(file_path, "r") as f:
            return json.load(f)

    @staticmethod
    def write_csv(file_path, rows, headers=None):
        """
        Writes rows to a CSV file.
        """
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            if headers:
                writer.writerow(headers)
            writer.writerows(rows)

    @staticmethod
    def read_csv(file_path):
        """
        Reads rows from a CSV file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found")
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            return [row for row in reader]

    @staticmethod
    def compress_file(file_path, output_path=None):
        """
        Compresses a file using gzip.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found")
        output_path = output_path or f"{file_path}.gz"
        with open(file_path, "rb") as f_in, gzip.open(output_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        return output_path

    @staticmethod
    def decompress_file(file_path, output_path=None):
        """
        Decompresses a gzip file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found")
        output_path = output_path or file_path.replace(".gz", "")
        with gzip.open(file_path, "rb") as f_in, open(output_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        return output_path

    @staticmethod
    def delete_file(file_path):
        """
        Deletes a file.
        """
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

    @staticmethod
    def rename_file(file_path, new_name):
        """
        Renames a file.
        """
        if os.path.exists(file_path):
            os.rename(file_path, new_name)
        else:
            raise FileNotFoundError(f"{file_path} not found")

class TaskScheduler:
    """
    Schedule tasks on the system using cron jobs (for Linux/macOS).
    """

    def __init__(self, user=True):
        """
        Initialize the scheduler.
        :param user: If True, uses the current user's crontab; otherwise, uses the system-wide crontab.
        """
        self.cron = CronTab(user=user)

    def add_job(self, command, schedule, comment=None):
        """
        Add a new cron job.
        :param command: Command to execute.
        :param schedule: Schedule as a tuple (minute, hour, day, month, day_of_week).
        :param comment: Optional comment to identify the job.
        """
        job = self.cron.new(command=command, comment=comment)
        minute, hour, day, month, day_of_week = schedule
        job.setall(minute, hour, day, month, day_of_week)
        self.cron.write()
        return job

    def remove_job(self, comment):
        """
        Remove a job based on its comment.
        :param comment: The comment identifying the job to remove.
        """
        self.cron.remove_all(comment=comment)
        self.cron.write()

    def list_jobs(self):
        """
        List all existing cron jobs.
        """
        return [job for job in self.cron]

class TaskScheduler:
    """
    Schedule tasks on the system using cron jobs (for Linux/macOS).
    """

    def __init__(self, user=True):
        """
        Initialize the scheduler.
        :param user: If True, uses the current user's crontab; otherwise, uses the system-wide crontab.
        """
        self.cron = CronTab(user=user)

    def add_job(self, command, schedule, comment=None):
        """
        Add a new cron job.
        :param command: Command to execute.
        :param schedule: Schedule as a tuple (minute, hour, day, month, day_of_week).
        :param comment: Optional comment to identify the job.
        """
        job = self.cron.new(command=command, comment=comment)
        minute, hour, day, month, day_of_week = schedule
        job.setall(minute, hour, day, month, day_of_week)
        self.cron.write()
        return job

    def remove_job(self, comment):
        """
        Remove a job based on its comment.
        :param comment: The comment identifying the job to remove.
        """
        self.cron.remove_all(comment=comment)
        self.cron.write()

    def list_jobs(self):
        """
        List all existing cron jobs.
        """
        return [job for job in self.cron]

class EnvManager:
    """
    Load and manage environment variables from `.env` files without using the dotenv library.
    """

    @staticmethod
    def load_env(env_file=".env"):
        """
        Load environment variables from a `.env` file manually.
        """
        if not os.path.exists(env_file):
            raise FileNotFoundError(f"{env_file} not found")
        with open(env_file, "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value

    @staticmethod
    def get_env_var(key, default=None):
        """
        Get the value of an environment variable.
        :param key: Environment variable key.
        :param default: Default value if the variable is not found.
        """
        return os.getenv(key, default)

    @staticmethod
    def set_env_var(key, value, env_file=".env"):
        """
        Set a new environment variable in memory and update the `.env` file.
        :param key: Environment variable key.
        :param value: Environment variable value.
        :param env_file: Path to the `.env` file.
        """
        os.environ[key] = value
        with open(env_file, "a") as f:
            f.write(f"{key}={value}\n")

class FileSync:
    """
    Sync files between local and remote systems or directories.
    """

    @staticmethod
    def sync_directories(source, destination):
        """
        Sync two directories.
        :param source: Source directory.
        :param destination: Destination directory.
        """
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source directory '{source}' not found")
        shutil.copytree(source, destination, dirs_exist_ok=True)

    @staticmethod
    def sync_with_remote(local_dir, remote_dir, remote_host, user, direction="push"):
        """
        Sync a local directory with a remote directory using `rsync`.
        :param local_dir: Local directory path.
        :param remote_dir: Remote directory path.
        :param remote_host: Hostname or IP of the remote machine.
        :param user: Remote system's username.
        :param direction: Either "push" (local to remote) or "pull" (remote to local).
        """
        if direction == "push":
            command = f"rsync -avz {local_dir}/ {user}@{remote_host}:{remote_dir}"
        elif direction == "pull":
            command = f"rsync -avz {user}@{remote_host}:{remote_dir}/ {local_dir}"
        else:
            raise ValueError("Direction must be 'push' or 'pull'")

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Sync failed: {result.stderr}")
        return result.stdout

class BackgroundJob:
    """
    Background job execution using subprocess.
    """

    @staticmethod
    def execute_in_background(command, log_file="job.log"):
        """
        Execute a command as a background job and redirect output to a log file.
        :param command: Command to execute.
        :param log_file: Log file to store the output.
        """
        with open(log_file, "w") as log:
            subprocess.Popen(command, shell=True, stdout=log, stderr=log)

    @staticmethod
    def run_periodically(command, interval):
        """
        Execute a command periodically.
        :param command: Command to execute.
        :param interval: Interval in seconds.
        """
        while True:
            subprocess.run(command, shell=True)
            time.sleep(interval)

class APIClient:
    """
    A reusable API client for making HTTP requests to third-party APIs.
    """

    def __init__(self, base_url, headers=None, timeout=30):
        """
        Initialize the API client.
        :param base_url: Base URL for the API.
        :param headers: Default headers to include with every request.
        :param timeout: Timeout for API requests in seconds.
        """
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.timeout = timeout

    def _make_request(self, method, endpoint, **kwargs):
        """
        Make an HTTP request to the API.
        :param method: HTTP method (GET, POST, etc.).
        :param endpoint: API endpoint relative to the base URL.
        :return: Response object.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.request(
                method=method, url=url, headers=self.headers, timeout=self.timeout, **kwargs
            )
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.json()  # Parse JSON response
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")

    def get(self, endpoint, params=None):
        """Make a GET request."""
        return self._make_request("GET", endpoint, params=params)

    def post(self, endpoint, data=None, json_data=None):
        """Make a POST request."""
        return self._make_request("POST", endpoint, data=data, json=json_data)

    def put(self, endpoint, data=None, json_data=None):
        """Make a PUT request."""
        return self._make_request("PUT", endpoint, data=data, json=json_data)

    def delete(self, endpoint):
        """Make a DELETE request."""
        return self._make_request("DELETE", endpoint)

class WebhookManager:
    """
    A utility class for managing and validating webhooks.
    """

    @staticmethod
    def verify_signature(secret, payload, signature, algorithm="sha256"):
        """
        Verify the signature of a webhook payload.
        :param secret: Shared secret key.
        :param payload: The raw webhook payload.
        :param signature: The received signature to verify.
        :param algorithm: The hashing algorithm to use (default: sha256).
        :return: True if the signature is valid, False otherwise.
        """
        computed_signature = hmac.new(
            key=secret.encode(), msg=payload.encode(), digestmod=getattr(hashlib, algorithm)
        ).hexdigest()
        return hmac.compare_digest(computed_signature, signature)

    @staticmethod
    def send_webhook(url, payload, headers=None):
        """
        Send a webhook payload to a specified URL.
        :param url: Webhook URL.
        :param payload: Data to send in the webhook.
        :param headers: Optional headers to include in the request.
        :return: Response object.
        """
        headers = headers or {"Content-Type": "application/json"}
        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to send webhook: {e}")

class OAuthManager:
    """
    A helper class for OAuth2 authentication flows.
    """

    def __init__(self, client_id, client_secret, auth_url, token_url, redirect_uri):
        """
        Initialize the OAuth manager.
        :param client_id: OAuth2 client ID.
        :param client_secret: OAuth2 client secret.
        :param auth_url: Authorization URL for user login.
        :param token_url: Token URL for exchanging codes for tokens.
        :param redirect_uri: Redirect URI after authentication.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_url = auth_url
        self.token_url = token_url
        self.redirect_uri = redirect_uri

    def get_auth_url(self, state=None, scope=None):
        """
        Generate the URL for user authentication.
        :param state: Optional state parameter for CSRF protection.
        :param scope: Optional scope for permissions.
        :return: Authentication URL.
        """
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
        }
        if state:
            params["state"] = state
        if scope:
            params["scope"] = " ".join(scope)

        query_string = "&".join(f"{k}={v}" for k, v in params.items())
        return f"{self.auth_url}?{query_string}"

    def exchange_code_for_token(self, code):
        """
        Exchange an authorization code for an access token.
        :param code: Authorization code received from the auth server.
        :return: Access token data as a dictionary.
        """
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri,
        }
        try:
            response = requests.post(self.token_url, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Token exchange failed: {e}")

class APIClient:
    """
    A reusable API client for interacting with third-party RESTful APIs.
    """

    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None, timeout: int = 30):
        """
        Initialize the API client.
        :param base_url: Base URL for the API.
        :param headers: Default headers for requests.
        :param timeout: Request timeout in seconds.
        """
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.timeout = timeout

    def _make_request(self, method: str, endpoint: str, **kwargs):
        """
        Internal helper for making HTTP requests.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.request(
                method=method, url=url, headers=self.headers, timeout=self.timeout, **kwargs
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request error: {e}")

    def get(self, endpoint: str, params: Optional[Dict] = None):
        """Perform a GET request."""
        return self._make_request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict] = None, json_data: Optional[Dict] = None):
        """Perform a POST request."""
        return self._make_request("POST", endpoint, data=data, json=json_data)

    def put(self, endpoint: str, data: Optional[Dict] = None, json_data: Optional[Dict] = None):
        """Perform a PUT request."""
        return self._make_request("PUT", endpoint, data=data, json=json_data)

    def delete(self, endpoint: str):
        """Perform a DELETE request."""
        return self._make_request("DELETE", endpoint)

class WebhookManager:
    """
    Tools for sending and verifying webhooks.
    """

    @staticmethod
    def verify_signature(secret: str, payload: str, signature: str, algorithm: str = "sha256") -> bool:
        """
        Verify the HMAC signature of a webhook payload.
        :param secret: Shared secret key.
        :param payload: Raw payload string.
        :param signature: Received signature for validation.
        :param algorithm: Hashing algorithm (default: sha256).
        :return: True if the signature matches, False otherwise.
        """
        computed_signature = hmac.new(
            key=secret.encode(), msg=payload.encode(), digestmod=getattr(hashlib, algorithm)
        ).hexdigest()
        return hmac.compare_digest(computed_signature, signature)

    @staticmethod
    def send_webhook(url: str, payload: Dict, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Send a webhook payload to a given URL.
        :param url: Target webhook URL.
        :param payload: JSON payload to send.
        :param headers: Optional headers for the request.
        :return: Response object.
        """
        headers = headers or {"Content-Type": "application/json"}
        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to send webhook: {e}")

class OAuthManager:
    """
    Helper class for handling OAuth2 authentication flows.
    """

    def __init__(self, client_id: str, client_secret: str, auth_url: str, token_url: str, redirect_uri: str):
        """
        Initialize the OAuth manager.
        :param client_id: OAuth2 client ID.
        :param client_secret: OAuth2 client secret.
        :param auth_url: Authorization endpoint URL.
        :param token_url: Token exchange endpoint URL.
        :param redirect_uri: Redirect URI after user authentication.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_url = auth_url
        self.token_url = token_url
        self.redirect_uri = redirect_uri

    def get_auth_url(self, state: Optional[str] = None, scope: Optional[List[str]] = None) -> str:
        """
        Generate the authorization URL for user login.
        :param state: Optional state parameter for CSRF protection.
        :param scope: List of permissions.
        :return: Authorization URL.
        """
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
        }
        if state:
            params["state"] = state
        if scope:
            params["scope"] = " ".join(scope)
        query_string = "&".join(f"{k}={v}" for k, v in params.items())
        return f"{self.auth_url}?{query_string}"

    def exchange_code_for_token(self, code: str) -> Dict:
        """
        Exchange an authorization code for an access token.
        :param code: Authorization code from the auth server.
        :return: Access token and related information.
        """
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri,
        }
        try:
            response = requests.post(self.token_url, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Token exchange error: {e}")

class TestingUtils:
    """
    Utilities for testing and debugging.
    """

    @staticmethod
    def generate_test_data(schema: Dict[str, Any], num_samples: int = 10) -> List[Dict[str, Any]]:
        """
        Generate test data based on a schema.
        :param schema: A dictionary defining field names and types.
        :param num_samples: Number of test samples to generate.
        :return: A list of dictionaries containing test data.
        """
        fake = Faker()
        test_data = []

        for _ in range(num_samples):
            sample = {}
            for field, field_type in schema.items():
                if field_type == "name":
                    sample[field] = fake.name()
                elif field_type == "email":
                    sample[field] = fake.email()
                elif field_type == "phone":
                    sample[field] = fake.phone_number()
                elif field_type == "address":
                    sample[field] = fake.address()
                elif field_type == "date":
                    sample[field] = fake.date()
                elif field_type == "text":
                    sample[field] = fake.text(max_nb_chars=100)
                else:
                    sample[field] = "Unknown"
            test_data.append(sample)

        return test_data

    @staticmethod
    def measure_execution_time(func):
        """
        Decorator to measure the execution time of a function.
        :param func: Function to measure.
        """
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper

    @staticmethod
    def memory_usage_report(obj: Any) -> str:
        """
        Estimate the memory usage of an object.
        :param obj: Python object.
        :return: Human-readable memory usage string.
        """
        import sys
        size = sys.getsizeof(obj)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

class LocalizationUtils:
    """
    Utilities for localization and internationalization.
    """

    @staticmethod
    def set_locale(language_code: str):
        """
        Set the locale for the application.
        :param language_code: Language code (e.g., 'en_US', 'fr_FR').
        """
        try:
            locale.setlocale(locale.LC_ALL, language_code)
        except locale.Error as e:
            raise ValueError(f"Invalid locale '{language_code}': {e}")

    @staticmethod
    def format_date(dt: datetime, locale_code: str = "en_US", date_format: str = "long") -> str:
        """
        Format a date in a specific locale.
        :param dt: The datetime object to format.
        :param locale_code: Locale code (e.g., 'en_US', 'fr_FR').
        :param date_format: Date format ('short', 'medium', 'long', 'full').
        :return: Formatted date string.
        """
        return dates.format_date(dt, format=date_format, locale=locale_code)

    @staticmethod
    def format_number(number: float, locale_code: str = "en_US") -> str:
        """
        Format a number in a specific locale.
        :param number: The number to format.
        :param locale_code: Locale code (e.g., 'en_US', 'de_DE').
        :return: Formatted number string.
        """
        return numbers.format_decimal(number, locale=locale_code)

    @staticmethod
    def convert_currency(amount: float, from_currency: str, to_currency: str, exchange_rate: float) -> str:
        """
        Convert an amount between currencies and format it.
        :param amount: Amount to convert.
        :param from_currency: Source currency code (e.g., 'USD').
        :param to_currency: Target currency code (e.g., 'EUR').
        :param exchange_rate: Conversion rate.
        :return: Formatted currency string.
        """
        converted = amount * exchange_rate
        return f"{from_currency} {amount:,.2f} → {to_currency} {converted:,.2f}"

class DatabaseSchemaExtractor:
    """
    Extract database schema information for SQLite, MySQL, and PostgreSQL.
    """

    @staticmethod
    def extract_schema(db_type: str, connection_details: Dict[str, Any], table_name: str) -> List[Dict[str, Any]]:
        """
        Extract schema information for a table.
        :param db_type: Type of the database ('sqlite', 'mysql', 'postgresql').
        :param connection_details: Database connection details (e.g., path, host, user, password).
        :param table_name: Name of the table to extract schema from.
        :return: A list of column information.
        """
        if db_type == "sqlite":
            return DatabaseSchemaExtractor._extract_sqlite_schema(connection_details["db_path"], table_name)
        elif db_type == "mysql":
            return DatabaseSchemaExtractor._extract_mysql_schema(connection_details, table_name)
        elif db_type == "postgresql":
            return DatabaseSchemaExtractor._extract_postgresql_schema(connection_details, table_name)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

    @staticmethod
    def _extract_sqlite_schema(db_path: str, table_name: str) -> List[Dict[str, Any]]:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        schema = [{"name": row[1], "type": row[2]} for row in cursor.fetchall()]
        conn.close()
        return schema

    @staticmethod
    def _extract_mysql_schema(connection_details: Dict[str, Any], table_name: str) -> List[Dict[str, Any]]:
        conn = pymysql.connect(
            host=connection_details["host"],
            user=connection_details["user"],
            password=connection_details["password"],
            database=connection_details["database"],
        )
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        schema = [{"name": row[0], "type": row[1]} for row in cursor.fetchall()]
        conn.close()
        return schema

    @staticmethod
    def _extract_postgresql_schema(connection_details: Dict[str, Any], table_name: str) -> List[Dict[str, Any]]:
        conn = pg8000.connect(
            host=connection_details["host"],
            user=connection_details["user"],
            password=connection_details["password"],
            database=connection_details["database"],
        )
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = %s
        """, (table_name,))
        schema = [{"name": row[0], "type": row[1]} for row in cursor.fetchall()]
        conn.close()
        return schema

class AutomatedTestSuiteGenerator:
    """
    Generate automated test suites from database schemas.
    """

    @staticmethod
    def generate_test_cases(schema: List[Dict[str, Any]], num_cases: int = 10) -> List[Dict[str, Any]]:
        """
        Generate test cases based on a table schema.
        :param schema: List of column information from the schema.
        :param num_cases: Number of test cases to generate.
        :return: List of dictionaries representing test cases.
        """
        faker = Faker()
        test_cases = []

        for _ in range(num_cases):
            case = {}
            for column in schema:
                col_name = column["name"]
                col_type = column["type"].lower()
                if "int" in col_type:
                    case[col_name] = faker.random_int()
                elif "char" in col_type or "text" in col_type:
                    case[col_name] = faker.text(max_nb_chars=20)
                elif "date" in col_type or "time" in col_type:
                    case[col_name] = faker.date_time_this_century().strftime("%Y-%m-%d %H:%M:%S")
                else:
                    case[col_name] = None
            test_cases.append(case)

        return test_cases

    @staticmethod
    def generate_api_test_suite(base_url: str, endpoint: str, schema: List[Dict[str, Any]], num_cases: int = 10):
        """
        Generate a test suite for an API endpoint based on a database schema.
        :param base_url: Base URL for the API.
        :param endpoint: API endpoint (e.g., '/users').
        :param schema: List of column information from the schema.
        :param num_cases: Number of test cases to generate.
        """
        test_cases = AutomatedTestSuiteGenerator.generate_test_cases(schema, num_cases)
        headers = {"Content-Type": "application/json"}

        for idx, case in enumerate(test_cases, start=1):
            try:
                response = requests.post(f"{base_url}{endpoint}", json=case, headers=headers)
                print(f"Test Case {idx}: Status Code {response.status_code}, Response: {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Test Case {idx} failed: {e}")
