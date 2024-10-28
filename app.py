from JSPTH.ClasesCode import *
from JSPTH.Math.MainMath import MyMath
from JSPTH.Math.Trigonometry import Trigonometry
from JSPTH.Math.Algebra import Algebra
from JSPTH.Math.Time import Time
from JSPTH.Math.Geometry import GeometryMath as Geometry



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
print(Time.convert_time(5, 'days', 'hours'))
print(Time.date_difference("2023-01-01", "2023-01-10", unit="hours"))  
print(Time.add_time_to_date("2023-01-01", 7, "days")) 
print(Time.current_time_in_timezone(-5))  
print(Time.time_until_date("2024-12-25"))
print(Time.days_in_month(2024, 2))


# Example usages
print(AreaConverter.convert_area(1000, 'square_meters', 'acres'))  # Converts 1000 square meters to acres
print(AreaConverter.format_area(5000000))  # Formats 5,000,000 square meters into a human-readable string
print(AreaConverter.area_of_rectangle(10, 20, 'square_feet'))  # Area of a rectangle in square feet
print(AreaConverter.area_of_circle(5, 'square_inches'))  # Area of a circle in square inches
print(AreaConverter.area_of_triangle(10, 5, 'hectares'))  # Area of a triangle in hectares
