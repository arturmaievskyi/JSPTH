using System;
using System.Security.Cryptography;
using System.Text;

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
                public static double ConvertDistance(double value, string fromUnit, string toUnit)
            {
                var unitMap = new Dictionary<string, double>
            {
                { "m", 1 },        // Meter
                { "km", 1000 },    // Kilometer
                { "cm", 0.01 },    // Centimeter
                { "mm", 0.001 },   // Millimeter
                { "mi", 1609.34 }, // Mile
                { "yd", 0.9144 },  // Yard
                { "ft", 0.3048 },  // Foot
                { "in", 0.0254 }   // Inch
            };

                if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                    throw new ArgumentException("Invalid distance units specified.");

                return value * (unitMap[fromUnit] / unitMap[toUnit]);
            }

            // Temperature Converter
            public static double ConvertTemperature(double value, string fromUnit, string toUnit)
            {
                if (fromUnit == "C" && toUnit == "F") return value * 9 / 5 + 32;       // Celsius to Fahrenheit
                if (fromUnit == "F" && toUnit == "C") return (value - 32) * 5 / 9;     // Fahrenheit to Celsius
                if (fromUnit == "C" && toUnit == "K") return value + 273.15;          // Celsius to Kelvin
                if (fromUnit == "K" && toUnit == "C") return value - 273.15;          // Kelvin to Celsius
                if (fromUnit == "F" && toUnit == "K") return (value - 32) * 5 / 9 + 273.15; // Fahrenheit to Kelvin
                if (fromUnit == "K" && toUnit == "F") return (value - 273.15) * 9 / 5 + 32; // Kelvin to Fahrenheit

                if (fromUnit == toUnit) return value; // No conversion needed
                throw new ArgumentException("Invalid temperature units specified.");
            }

            // Pressure Converter
            public static double ConvertPressure(double value, string fromUnit, string toUnit)
            {
                var unitMap = new Dictionary<string, double>
            {
                { "Pa", 1 },        // Pascal
                { "kPa", 1000 },    // Kilopascal
                { "atm", 101325 },  // Atmosphere
                { "bar", 100000 },  // Bar
                { "psi", 6894.76 }, // Pounds per square inch
                { "torr", 133.322 } // Torr
            };

                if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                    throw new ArgumentException("Invalid pressure units specified.");

                return value * (unitMap[fromUnit] / unitMap[toUnit]);
            }

            // Energy Converter
            public static double ConvertEnergy(double value, string fromUnit, string toUnit)
            {
                var unitMap = new Dictionary<string, double>
            {
                { "J", 1 },         // Joule
                { "kJ", 1000 },     // Kilojoule
                { "cal", 4.184 },   // Calorie
                { "kcal", 4184 },   // Kilocalorie
                { "Wh", 3600 },     // Watt-hour
                { "kWh", 3600000 }, // Kilowatt-hour
                { "eV", 1.60218e-19 } // Electronvolt
            };

                if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                    throw new ArgumentException("Invalid energy units specified.");

                return value * (unitMap[fromUnit] / unitMap[toUnit]);
            }

            // Frequency Converter
            public static double ConvertFrequency(double value, string fromUnit, string toUnit)
            {
                var unitMap = new Dictionary<string, double>
            {
                { "Hz", 1 },        // Hertz
                { "kHz", 1000 },    // Kilohertz
                { "MHz", 1e6 },     // Megahertz
                { "GHz", 1e9 },     // Gigahertz
                { "THz", 1e12 }     // Terahertz
            };

                if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                    throw new ArgumentException("Invalid frequency units specified.");

                return value * (unitMap[fromUnit] / unitMap[toUnit]);
            }
        },
                public static double ConvertPower(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "W", 1 },         // Watt
                { "kW", 1000 },     // Kilowatt
                { "MW", 1e6 },      // Megawatt
                { "hp", 745.7 },    // Horsepower
                { "cal/s", 4.184 }, // Calories per second
                { "BTU/h", 0.293071 } // British Thermal Unit per hour
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid power units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }

        // Force Converter
        public static double ConvertForce(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "N", 1 },       // Newton
                { "kN", 1000 },   // Kilonewton
                { "dyn", 1e-5 },  // Dyne
                { "lbf", 4.44822 }, // Pound-force
                { "kgf", 9.80665 }  // Kilogram-force
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid force units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }

        // Torque Converter
        public static double ConvertTorque(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "Nm", 1 },         // Newton-meter
                { "kNm", 1000 },     // Kilonewton-meter
                { "lbft", 1.35582 }, // Pound-foot
                { "kgfm", 9.80665 }  // Kilogram-force meter
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid torque units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }

        // Density Converter
        public static double ConvertDensity(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "kg/m3", 1 },          // Kilogram per cubic meter
                { "g/cm3", 1000 },       // Gram per cubic centimeter
                { "lb/ft3", 16.0185 },   // Pound per cubic foot
                { "lb/in3", 27679.9 },   // Pound per cubic inch
                { "g/L", 1 },            // Gram per liter
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid density units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }

        // Luminance Converter
        public static double ConvertLuminance(double value, string fromUnit, string toUnit)
        {
            var unitMap = new Dictionary<string, double>
            {
                { "cd/m2", 1 },          // Candela per square meter
                { "nit", 1 },            // Nit (alias of cd/m2)
                { "foot-lambert", 3.426 }, // Foot-lambert
                { "stilb", 10000 },      // Stilb
                { "lambert", 3183.0988618 }, // Lambert
            };

            if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
                throw new ArgumentException("Invalid luminance units specified.");

            return value * (unitMap[fromUnit] / unitMap[toUnit]);
        }
        public static double ConvertFuelEfficiency(double value, string fromUnit, string toUnit)
    {
        var unitMap = new Dictionary<string, double>
            {
                { "mpg", 1 },                 // Miles per gallon
                { "kmpl", 2.35215 },          // Kilometers per liter
                { "L/100km", 235.214583 },    // Liters per 100 kilometers
            };

        if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
            throw new ArgumentException("Invalid fuel efficiency units specified.");

        return (value * unitMap[fromUnit]) / unitMap[toUnit];
    }

    // Radioactivity Converter
    public static double ConvertRadioactivity(double value, string fromUnit, string toUnit)
    {
        var unitMap = new Dictionary<string, double>
            {
                { "Bq", 1 },              // Becquerel
                { "Ci", 3.7e10 },         // Curie
                { "dps", 1 },             // Disintegrations per second (same as Becquerel)
                { "rutherford", 1e6 }     // Rutherford
            };

        if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
            throw new ArgumentException("Invalid radioactivity units specified.");

        return value * (unitMap[fromUnit] / unitMap[toUnit]);
    }

    // Data Transfer Rate Converter
    public static double ConvertDataTransferRate(double value, string fromUnit, string toUnit)
    {
        var unitMap = new Dictionary<string, double>
            {
                { "bps", 1 },            // Bits per second
                { "Kbps", 1e3 },         // Kilobits per second
                { "Mbps", 1e6 },         // Megabits per second
                { "Gbps", 1e9 },         // Gigabits per second
                { "Tbps", 1e12 },        // Terabits per second
                { "Bps", 8 },            // Bytes per second
                { "KBps", 8e3 },         // Kilobytes per second
                { "MBps", 8e6 },         // Megabytes per second
                { "GBps", 8e9 }          // Gigabytes per second
            };

        if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
            throw new ArgumentException("Invalid data transfer rate units specified.");

        return value * (unitMap[fromUnit] / unitMap[toUnit]);
    }

    // Capacitance Converter
    public static double ConvertCapacitance(double value, string fromUnit, string toUnit)
    {
        var unitMap = new Dictionary<string, double>
            {
                { "F", 1 },           // Farad
                { "mF", 1e-3 },       // Millifarad
                { "µF", 1e-6 },       // Microfarad
                { "nF", 1e-9 },       // Nanofarad
                { "pF", 1e-12 }       // Picofarad
            };

        if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
            throw new ArgumentException("Invalid capacitance units specified.");

        return value * (unitMap[fromUnit] / unitMap[toUnit]);
    }

    // Illumination Intensity Converter
    public static double ConvertIlluminationIntensity(double value, string fromUnit, string toUnit)
    {
        var unitMap = new Dictionary<string, double>
            {
                { "lux", 1 },            // Lux
                { "foot-candle", 10.7639 }, // Foot-candle
            };

        if (!unitMap.ContainsKey(fromUnit) || !unitMap.ContainsKey(toUnit))
            throw new ArgumentException("Invalid illumination intensity units specified.");

        return value * (unitMap[fromUnit] / unitMap[toUnit]);
    }
    }
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
    public static class CryptoUtils
    {
        // Hashing with SHA256
        public static string ComputeSHA256Hash(string input)
        {
            using (SHA256 sha256 = SHA256.Create())
            {
                byte[] bytes = Encoding.UTF8.GetBytes(input);
                byte[] hash = sha256.ComputeHash(bytes);
                return Convert.ToHexString(hash);
            }
        }

        // Symmetric encryption with AES
        public static (byte[] EncryptedData, byte[] Key, byte[] IV) EncryptAES(string plainText)
        {
            using (Aes aes = Aes.Create())
            {
                aes.GenerateKey();
                aes.GenerateIV();

                ICryptoTransform encryptor = aes.CreateEncryptor(aes.Key, aes.IV);

                using (var ms = new System.IO.MemoryStream())
                {
                    using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                    {
                        byte[] plainBytes = Encoding.UTF8.GetBytes(plainText);
                        cs.Write(plainBytes, 0, plainBytes.Length);
                    }
                    return (ms.ToArray(), aes.Key, aes.IV);
                }
            }
        }

        // Symmetric decryption with AES
        public static string DecryptAES(byte[] encryptedData, byte[] key, byte[] iv)
        {
            using (Aes aes = Aes.Create())
            {
                aes.Key = key;
                aes.IV = iv;

                ICryptoTransform decryptor = aes.CreateDecryptor(aes.Key, aes.IV);

                using (var ms = new System.IO.MemoryStream(encryptedData))
                {
                    using (var cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read))
                    {
                        using (var sr = new System.IO.StreamReader(cs))
                        {
                            return sr.ReadToEnd();
                        }
                    }
                }
            }
        }

        // RSA key pair generation
        public static (string PublicKey, string PrivateKey) GenerateRSAKeys()
        {
            using (RSA rsa = RSA.Create())
            {
                rsa.KeySize = 2048;
                string publicKey = Convert.ToBase64String(rsa.ExportSubjectPublicKeyInfo());
                string privateKey = Convert.ToBase64String(rsa.ExportPkcs8PrivateKey());
                return (publicKey, privateKey);
            }
        }

        // RSA encryption
        public static byte[] EncryptRSA(string plainText, string publicKeyBase64)
        {
            byte[] plainBytes = Encoding.UTF8.GetBytes(plainText);
            using (RSA rsa = RSA.Create())
            {
                rsa.ImportSubjectPublicKeyInfo(Convert.FromBase64String(publicKeyBase64), out _);
                return rsa.Encrypt(plainBytes, RSAEncryptionPadding.OaepSHA256);
            }
        }

        // RSA decryption
        public static string DecryptRSA(byte[] encryptedData, string privateKeyBase64)
        {
            using (RSA rsa = RSA.Create())
            {
                rsa.ImportPkcs8PrivateKey(Convert.FromBase64String(privateKeyBase64), out _);
                byte[] decryptedBytes = rsa.Decrypt(encryptedData, RSAEncryptionPadding.OaepSHA256);
                return Encoding.UTF8.GetString(decryptedBytes);
            }
        }

        // HMAC-SHA256
        public static string ComputeHMACSHA256(string input, string key)
        {
            using (HMACSHA256 hmac = new HMACSHA256(Encoding.UTF8.GetBytes(key)))
            {
                byte[] hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(input));
                return Convert.ToHexString(hash);
            }
        }
    
            public static string ComputeSHA512Hash(string input)
        {
            using (SHA512 sha512 = SHA512.Create())
            {
                byte[] bytes = Encoding.UTF8.GetBytes(input);
                byte[] hash = sha512.ComputeHash(bytes);
                return Convert.ToHexString(hash);
            }
        }

        // Key Derivation using PBKDF2
        public static byte[] DeriveKeyPBKDF2(string password, byte[] salt, int iterations, int keySize)
        {
            using (var rfc2898 = new Rfc2898DeriveBytes(password, salt, iterations, HashAlgorithmName.SHA256))
            {
                return rfc2898.GetBytes(keySize);
            }
        }

        // Digital Signature with ECDSA
        public static (string PublicKey, string PrivateKey) GenerateECDSAKeys()
        {
            using (ECDsa ecdsa = ECDsa.Create(ECCurve.NamedCurves.nistP256))
            {
                string publicKey = Convert.ToBase64String(ecdsa.ExportSubjectPublicKeyInfo());
                string privateKey = Convert.ToBase64String(ecdsa.ExportPkcs8PrivateKey());
                return (publicKey, privateKey);
            }
        }

        public static byte[] SignDataECDSA(string data, string privateKeyBase64)
        {
            using (ECDsa ecdsa = ECDsa.Create())
            {
                ecdsa.ImportPkcs8PrivateKey(Convert.FromBase64String(privateKeyBase64), out _);
                byte[] dataBytes = Encoding.UTF8.GetBytes(data);
                return ecdsa.SignData(dataBytes, HashAlgorithmName.SHA256);
            }
        }

        public static bool VerifySignatureECDSA(string data, byte[] signature, string publicKeyBase64)
        {
            using (ECDsa ecdsa = ECDsa.Create())
            {
                ecdsa.ImportSubjectPublicKeyInfo(Convert.FromBase64String(publicKeyBase64), out _);
                byte[] dataBytes = Encoding.UTF8.GetBytes(data);
                return ecdsa.VerifyData(dataBytes, signature, HashAlgorithmName.SHA256);
            }
        }

        // Symmetric Encryption with ChaCha20 (using BouncyCastle)
        public static byte[] EncryptChaCha20(string plainText, byte[] key, byte[] nonce)
        {
            if (key.Length != 32) throw new ArgumentException("Key must be 32 bytes for ChaCha20.");
            if (nonce.Length != 12) throw new ArgumentException("Nonce must be 12 bytes for ChaCha20.");

            var plaintextBytes = Encoding.UTF8.GetBytes(plainText);
            byte[] ciphertext = new byte[plaintextBytes.Length];

            using (var cipher = new Org.BouncyCastle.Crypto.Engines.ChaChaEngine())
            {
                cipher.Init(true, new Org.BouncyCastle.Crypto.Parameters.ParametersWithIV(
                    new Org.BouncyCastle.Crypto.Parameters.KeyParameter(key), nonce));
                cipher.ProcessBytes(plaintextBytes, 0, plaintextBytes.Length, ciphertext, 0);
            }

            return ciphertext;
        }

        public static string DecryptChaCha20(byte[] encryptedData, byte[] key, byte[] nonce)
        {
            if (key.Length != 32) throw new ArgumentException("Key must be 32 bytes for ChaCha20.");
            if (nonce.Length != 12) throw new ArgumentException("Nonce must be 12 bytes for ChaCha20.");

            byte[] plaintext = new byte[encryptedData.Length];

            using (var cipher = new Org.BouncyCastle.Crypto.Engines.ChaChaEngine())
            {
                cipher.Init(false, new Org.BouncyCastle.Crypto.Parameters.ParametersWithIV(
                    new Org.BouncyCastle.Crypto.Parameters.KeyParameter(key), nonce));
                cipher.ProcessBytes(encryptedData, 0, encryptedData.Length, plaintext, 0);
            }

            return Encoding.UTF8.GetString(plaintext);
        }
    }
},
    namespace BeckEnd
    {

    }
}