from datetime import datetime, timedelta

class Time:
    # Define conversion factors for time units in seconds
    units_in_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800
    }
    
    @staticmethod
    def convert_time(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a time value from one unit to another.
        """
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        # Check if units are valid
        if from_unit not in Time.units_in_seconds or to_unit not in Time.units_in_seconds:
            raise ValueError("Unsupported units. Choose from 'seconds', 'minutes', 'hours', 'days', or 'weeks'.")

        # Convert the value to seconds, then to the target unit
        value_in_seconds = value * Time.units_in_seconds[from_unit]
        converted_value = value_in_seconds / Time.units_in_seconds[to_unit]
        
        return converted_value
    
    @staticmethod
    def date_difference(date1: str, date2: str, unit: str = "days") -> float:
        """
        Calculate the difference between two dates in the specified unit.
        """
        unit = unit.lower()
        
        if unit not in Time.units_in_seconds:
            raise ValueError("Unsupported unit. Choose from 'seconds', 'minutes', 'hours', or 'days'.")
        
        # Parse date strings to datetime objects
        date_format = "%Y-%m-%d"
        try:
            date1_obj = datetime.strptime(date1, date_format)
            date2_obj = datetime.strptime(date2, date_format)
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        # Calculate the absolute difference in seconds and convert to the specified unit
        delta_seconds = abs((date2_obj - date1_obj).total_seconds())
        return delta_seconds / Time.units_in_seconds[unit]
    
    @staticmethod
    def add_time_to_date(date_str: str, amount: float, unit: str) -> str:
        """
        Add a specified amount of time to a date.
        """
        unit = unit.lower()
        
        if unit not in Time.units_in_seconds:
            raise ValueError("Unsupported unit. Choose from 'seconds', 'minutes', 'hours', 'days', or 'weeks'.")
        
        # Parse date string to a datetime object
        date_format = "%Y-%m-%d"
        try:
            date_obj = datetime.strptime(date_str, date_format)
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        # Calculate the time delta and add it to the date
        delta = timedelta(seconds=amount * Time.units_in_seconds[unit])
        new_date = date_obj + delta
        return new_date.strftime(date_format)
    
    @staticmethod
    def current_time_in_timezone(timezone_offset: int) -> str:
        """
        Get the current time in a specified timezone (offset in hours from UTC).
        """
        utc_now = datetime.utcnow()
        timezone_time = utc_now + timedelta(hours=timezone_offset)
        return timezone_time.strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def time_until_date(target_date: str) -> str:
        """
        Get the time remaining until a specific date.
        """
        date_format = "%Y-%m-%d"
        try:
            target_date_obj = datetime.strptime(target_date, date_format)
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        current_date = datetime.now()
        if current_date > target_date_obj:
            return "The target date has already passed."
        
        remaining_time = target_date_obj - current_date
        days, seconds = remaining_time.days, remaining_time.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        
        return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds remaining"
    
    @staticmethod
    def days_in_month(year: int, month: int) -> int:
        """
        Return the number of days in a specific month and year.
        """
        # Check if month is valid
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        
        # Handle February and leap years
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        current_month = datetime(year, month, 1)
        
        return (next_month - current_month).days
