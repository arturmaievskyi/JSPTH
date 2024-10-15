from JSPTH.ClasesCode import Console
from JSPTH.Math.MainMath import MyMath as Math

test_a = int(Console.IntGet("First num "))
test_b = int(Console.IntGet("Second num "))

Math.add(test_a, test_b)
Math.square_number(test_a)
Math.square_number(test_b)