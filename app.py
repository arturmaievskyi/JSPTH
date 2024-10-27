from JSPTH.ClasesCode import Console
from JSPTH.Math import MyMath, Trigonometry, Geometry, Time


MyMath.factorial(9)

test = Console.IntGet("Your num:")


Console.log(test)
print(MyMath.add(test, test))

print(MyMath.divide_numbers(test, 10))
print(MyMath.square_number(test))
print(MyMath.root(9))
print(Geometry.area_of_circle(10))

print(Geometry.circumference_of_circle(10))


print(Geometry.distance_between_points(1, 2, 3, 4))
# Example usages
print(Time.convert_time(5, 'days', 'hours'))  # Converts 5 days to hours
print(Time.date_difference("2023-01-01", "2023-01-10", unit="hours"))  # Difference in hours between two dates
print(Time.add_time_to_date("2023-01-01", 7, "days"))  # Adds 7 days to a date
print(Time.current_time_in_timezone(-5))  # Gets the current time in UTC-5
print(Time.time_until_date("2024-12-25"))  # Time until Christmas 2024
print(Time.days_in_month(2024, 2))  # Days in February for a leap year
