from JSPTH.ClasesCode import Console
from JSPTH.Math.MainMath import MyMath as Math
from JSPTH.Math.Geometry import GeometryMath as Gm
from JSPTH.Math.Trigonometry import Trigonometry as Tr


Math.factorial(9)

test = Console.IntGet("Your num:")


Console.log(test)
print(Math.add(test, test))

print(Math.divide_numbers(test, 10))
print(Math.square_number(test))
print(Math.root(9))
print(Gm.area_of_circle(10))

print(Gm.circumference_of_circle(10))


print(Gm.distance_between_points(1, 2, 3, 4))
