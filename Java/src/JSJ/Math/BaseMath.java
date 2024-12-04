package JSJ.Math;

class BaseMath{

    /**
     * Adds two numbers.
     *
     * @param a First number.
     * @param b Second number.
     * @return Sum of a and b.
     */
    public static double add(double a, double b) {
        return a + b;
    }

    /**
     * Subtracts two numbers.
     *
     * @param a First number.
     * @param b Second number.
     * @return Difference of a and b.
     */
    public static double subtract(double a, double b) {
        return a - b;
    }

    /**
     * Multiplies two numbers.
     *
     * @param a First number.
     * @param b Second number.
     * @return Product of a and b.
     */
    public static double multiply(double a, double b) {
        return a * b;
    }

    /**
     * Divides two numbers.
     *
     * @param a Dividend.
     * @param b Divisor.
     * @return Quotient of a divided by b.
     * @throws ArithmeticException If b is zero.
     */
    public static double divide(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero is not allowed.");
        }
        return a / b;
    }

    /**
     * Calculates the power of a number.
     *
     * @param base The base number.
     * @param exponent The exponent.
     * @return Result of base raised to the power of exponent.
     */
    public static double power(double base, double exponent) {
        return Math.pow(base, exponent);
    }

    /**
     * Calculates the square root of a number.
     *
     * @param a The number.
     * @return Square root of a.
     */
    public static double squareRoot(double a) {
        if (a < 0) {
            throw new ArithmeticException("Square root of negative numbers is not supported.");
        }
        return Math.sqrt(a);
    }

    /**
     * Calculates the factorial of a number.
     *
     * @param n Non-negative integer.
     * @return Factorial of n.
     * @throws IllegalArgumentException If n is negative.
     */
    public static long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Factorial of negative numbers is not defined.");
        }
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    /**
     * Calculates the greatest common divisor (GCD) of two integers.
     *
     * @param a First integer.
     * @param b Second integer.
     * @return GCD of a and b.
     */
    public static int gcd(int a, int b) {
        if (b == 0) {
            return Math.abs(a);
        }
        return gcd(b, a % b);
    }
}