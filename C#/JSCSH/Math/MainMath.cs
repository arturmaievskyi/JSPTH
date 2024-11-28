// File: MathOperations.cs
using System;

namespace MathUtilities
{
    public static class MathOperations
    {
        // Adds two numbers
        public static double Add(double a, double b)
        {
            return a + b;
        }

        // Subtracts the second number from the first
        public static double Subtract(double a, double b)
        {
            return a - b;
        }

        // Multiplies two numbers
        public static double Multiply(double a, double b)
        {
            return a * b;
        }

        // Divides the first number by the second (with error handling for division by zero)
        public static double Divide(double a, double b)
        {
            if (b == 0)
            {
                throw new ArgumentException("Division by zero is not allowed.");
            }
            return a / b;
        }

        // Squares a number
        public static double Square(double a)
        {
            return a * a;
        }

        // Calculates the square root of a number
        public static double Root(double a)
        {
            if (a < 0)
            {
                throw new ArgumentException("Cannot calculate the square root of a negative number.");
            }
            return Math.Sqrt(a);
        }

        // Calculates the factorial of a number (non-negative integer)
        public static long Factorial(int n)
        {
            if (n < 0)
            {
                throw new ArgumentException("Factorial is not defined for negative numbers.");
            }

            long result = 1;
            for (int i = 2; i <= n; i++)
            {
                result *= i;
            }
            return result;
        }
    }
}
