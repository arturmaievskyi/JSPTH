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

    public static class Trigonometry
    {
        private const double DegToRad = Math.PI / 180.0; // Conversion factor from degrees to radians
        private const double RadToDeg = 180.0 / Math.PI; // Conversion factor from radians to degrees

        // Trigonometric functions
        public static double Sine(double angleDegrees) => Math.Sin(angleDegrees * DegToRad);

        public static double Cosine(double angleDegrees) => Math.Cos(angleDegrees * DegToRad);

        public static double Tangent(double angleDegrees) => Math.Tan(angleDegrees * DegToRad);

        public static double Arcsine(double value) => RadToDeg * Math.Asin(value);

        public static double Arccosine(double value) => RadToDeg * Math.Acos(value);

        public static double Arctangent(double value) => RadToDeg * Math.Atan(value);

        // Reciprocal trigonometric functions
        public static double Secant(double angleDegrees) => 1 / Cosine(angleDegrees);

        public static double Cosecant(double angleDegrees) => 1 / Sine(angleDegrees);

        public static double Cotangent(double angleDegrees) => 1 / Tangent(angleDegrees);

        // Trigonometric laws
        public static double LawOfCosines(double a, double b, double angleDegrees)
        {
            double angleRadians = angleDegrees * DegToRad;
            return Math.Sqrt(a * a + b * b - 2 * a * b * Math.Cos(angleRadians));
        }

        public static double LawOfSines(double a, double angleADegrees, double angleBDegrees)
        {
            double angleARadians = angleADegrees * DegToRad;
            double angleBRadians = angleBDegrees * DegToRad;
            return (a * Math.Sin(angleBRadians)) / Math.Sin(angleARadians);
        }

        // Sum and double angle formulas
        public static double SineSum(double angleA, double angleB)
        {
            double radA = angleA * DegToRad;
            double radB = angleB * DegToRad;
            return Math.Sin(radA) * Math.Cos(radB) + Math.Cos(radA) * Math.Sin(radB);
        }

        public static double CosineSum(double angleA, double angleB)
        {
            double radA = angleA * DegToRad;
            double radB = angleB * DegToRad;
            return Math.Cos(radA) * Math.Cos(radB) - Math.Sin(radA) * Math.Sin(radB);
        }

        public static double TangentSum(double angleA, double angleB)
        {
            double radA = angleA * DegToRad;
            double radB = angleB * DegToRad;
            return (Math.Tan(radA) + Math.Tan(radB)) / (1 - Math.Tan(radA) * Math.Tan(radB));
        }

        public static double SineDouble(double angleDegrees)
        {
            double rad = angleDegrees * DegToRad;
            return 2 * Math.Sin(rad) * Math.Cos(rad);
        }

        public static double CosineDouble(double angleDegrees)
        {
            double rad = angleDegrees * DegToRad;
            return Math.Cos(rad) * Math.Cos(rad) - Math.Sin(rad) * Math.Sin(rad);
        }

        public static double TangentDouble(double angleDegrees)
        {
            double rad = angleDegrees * DegToRad;
            return 2 * Math.Tan(rad) / (1 - Math.Tan(rad) * Math.Tan(rad));
        }

        // Coordinate conversions
        public static (double X, double Y) PolarToCartesian(double radius, double angleDegrees)
        {
            double angleRadians = angleDegrees * DegToRad;
            double x = radius * Math.Cos(angleRadians);
            double y = radius * Math.Sin(angleRadians);
            return (x, y);
        }

        public static (double Radius, double AngleDegrees) CartesianToPolar(double x, double y)
        {
            double radius = Math.Sqrt(x * x + y * y);
            double angleRadians = Math.Atan2(y, x);
            return (radius, angleRadians * RadToDeg);
        }
    }
}
