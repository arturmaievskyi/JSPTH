using System;


namespace JSCSH
{
    namespace convertors
    {
        public static class Converters
    {
        // Storage Converter
        public static double ConvertStorage(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "B", 1 },            // Byte
                { "KB", 1024 },        // Kilobyte
                { "MB", 1024 * 1024 }, // Megabyte
                { "GB", 1024 * 1024 * 1024 }, // Gigabyte
                { "TB", Math.Pow(1024, 4) }   // Terabyte
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid storage units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }

        // Area Converter
        public static double ConvertArea(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "m2", 1 },      // Square Meter
                { "km2", 1e6 },   // Square Kilometer
                { "ft2", 0.092903 }, // Square Foot
                { "yd2", 0.836127 }, // Square Yard
                { "acre", 4046.86 }, // Acre
                { "ha", 10000 }   // Hectare
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid area units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }

        // Volume Converter
        public static double ConvertVolume(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "m3", 1 },        // Cubic Meter
                { "cm3", 1e-6 },    // Cubic Centimeter
                { "litre", 0.001 }, // Liter
                { "gallon", 0.00378541 }, // US Gallon
                { "quart", 0.000946353 }, // US Quart
                { "pint", 0.000473176 }   // US Pint
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid volume units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }

        // Speed Converter
        public static double ConvertSpeed(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "mps", 1 },         // Meters per second
                { "kph", 0.277778 },  // Kilometers per hour
                { "mph", 0.44704 },   // Miles per hour
                { "fps", 0.3048 },    // Feet per second
                { "knots", 0.514444 } // Knots
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid speed units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }

        // Mass Converter
        public static double ConvertMass(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "g", 1 },           // Gram
                { "kg", 1000 },       // Kilogram
                { "mg", 0.001 },      // Milligram
                { "lb", 453.592 },    // Pound
                { "oz", 28.3495 },    // Ounce
                { "ton", 1e6 }        // Metric Ton
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid mass units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        },


    }
    },
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
        public static class GeometryOperations
        {
            private const double Pi = Math.PI;

            // Circle properties
            public static double CircleArea(double radius)
            {
                if (radius < 0) throw new ArgumentException("Radius cannot be negative.");
                return Pi * radius * radius;
            }

            public static double CircleCircumference(double radius)
            {
                if (radius < 0) throw new ArgumentException("Radius cannot be negative.");
                return 2 * Pi * radius;
            }

            // Cone properties
            public static double VolumeOfCone(double radius, double height)
            {
                if (radius < 0 || height < 0) throw new ArgumentException("Radius and height must be non-negative.");
                return (1.0 / 3) * Pi * radius * radius * height;
            }

            public static double SurfaceAreaOfCone(double radius, double slantHeight)
            {
                if (radius < 0 || slantHeight < 0) throw new ArgumentException("Radius and slant height must be non-negative.");
                return Pi * radius * (radius + slantHeight);
            }

            // Distance between two points
            public static double DistanceBetweenPoints(double x1, double y1, double x2, double y2)
            {
                double deltaX = x2 - x1;
                double deltaY = y2 - y1;
                return Math.Sqrt(deltaX * deltaX + deltaY * deltaY);
            }

            // Triangle area using Heron's formula
            public static double TriangleAreaHeron(double a, double b, double c)
            {
                if (a <= 0 || b <= 0 || c <= 0) throw new ArgumentException("Sides must be positive.");
                double s = (a + b + c) / 2; // Semi-perimeter
                return Math.Sqrt(s * (s - a) * (s - b) * (s - c));
            }

            // Parallelogram area
            public static double ParallelogramArea(double baseLength, double height)
            {
                if (baseLength < 0 || height < 0) throw new ArgumentException("Base length and height must be non-negative.");
                return baseLength * height;
            }

            // Sphere properties
            public static double SphereSurfaceArea(double radius)
            {
                if (radius < 0) throw new ArgumentException("Radius cannot be negative.");
                return 4 * Pi * radius * radius;
            }

            public static double SphereVolume(double radius)
            {
                if (radius < 0) throw new ArgumentException("Radius cannot be negative.");
                return (4.0 / 3) * Pi * radius * radius * radius;
            }

            // Circle area and circumference (aliases for consistency)
            public static double AreaOfCircle(double radius) => CircleArea(radius);

            public static double CircumferenceOfCircle(double radius) => CircleCircumference(radius);
        }
        public static class AlgebraOperations
        {
            // Solves a quadratic equation ax^2 + bx + c = 0
            public static (double? Root1, double? Root2) QuadraticSolver(double a, double b, double c)
            {
                if (a == 0) throw new ArgumentException("Coefficient 'a' cannot be zero for a quadratic equation.");
                double discriminant = b * b - 4 * a * c;
                if (discriminant < 0) return (null, null); // No real roots
                double root1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
                double root2 = (-b - Math.Sqrt(discriminant)) / (2 * a);
                return (root1, root2);
            }

            // Solves a linear equation ax + b = 0
            public static double LinearSolver(double a, double b)
            {
                if (a == 0) throw new ArgumentException("Coefficient 'a' cannot be zero for a linear equation.");
                return -b / a;
            }

            // Solves exponential equations of the form a^x = b
            public static double ExponentialSolver(double a, double b)
            {
                if (a <= 0 || b <= 0) throw new ArgumentException("Base and result must be positive.");
                return Math.Log(b) / Math.Log(a);
            }

            // Solves logarithmic equations of the form log_a(x) = b
            public static double LogarithmSolver(double a, double b)
            {
                if (a <= 0 || a == 1 || b <= 0) throw new ArgumentException("Base must be > 0 and ≠ 1; result must be positive.");
                return Math.Pow(a, b);
            }

            // Evaluates a polynomial at a given value of x
            public static double PolynomialEval(double[] coefficients, double x)
            {
                double result = 0;
                for (int i = 0; i < coefficients.Length; i++)
                {
                    result += coefficients[i] * Math.Pow(x, i);
                }
                return result;
            }

            // Computes the greatest common divisor (GCD) of two integers
            public static int GCD(int a, int b)
            {
                while (b != 0)
                {
                    int temp = b;
                    b = a % b;
                    a = temp;
                }
                return Math.Abs(a);
            }

            // Computes the least common multiple (LCM) of two integers
            public static int LCM(int a, int b)
            {
                if (a == 0 || b == 0) return 0;
                return Math.Abs(a * b) / GCD(a, b);
            }

            // Computes the binomial coefficient C(n, k) = n! / (k! * (n - k)!)
            public static long BinomialCoefficient(int n, int k)
            {
                if (n < 0 || k < 0 || k > n) throw new ArgumentException("Invalid values for n and k.");
                if (k == 0 || k == n) return 1;
                long result = 1;
                for (int i = 1; i <= k; i++)
                {
                    result = result * (n - i + 1) / i;
                }
                return result;
            }

            // Computes the nth term of an arithmetic progression
            public static double ArithmeticProgression(double firstTerm, double commonDifference, int n)
            {
                return firstTerm + (n - 1) * commonDifference;
            }

            // Computes the nth term of a geometric progression
            public static double GeometricProgression(double firstTerm, double commonRatio, int n)
            {
                return firstTerm * Math.Pow(commonRatio, n - 1);
            }

            // Computes the sum of the first n terms of a geometric series
            public static double GeometricSeriesSum(double firstTerm, double commonRatio, int n)
            {
                if (commonRatio == 1) return firstTerm * n;
                return firstTerm * (1 - Math.Pow(commonRatio, n)) / (1 - commonRatio);
            }
        }
    }
    namespace Crypto
    {

    },
    namespace BeckEnd
    {
        
    }
}