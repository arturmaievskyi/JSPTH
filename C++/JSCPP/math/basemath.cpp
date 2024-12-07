#include <cmath>
#include <stdexcept>

class BaseMath {
public:
    // Addition
    static double add(double a, double b) {
        return a + b;
    }

    // Subtraction
    static double subtract(double a, double b) {
        return a - b;
    }

    // Multiplication
    static double multiply(double a, double b) {
        return a * b;
    }

    // Division
    static double divide(double a, double b) {
        if (b == 0) throw std::invalid_argument("Division by zero is undefined.");
        return a / b;
    }

    // Power
    static double power(double base, double exponent) {
        return std::pow(base, exponent);
    }

    // Square Root
    static double square_root(double value) {
        if (value < 0) throw std::invalid_argument("Square root of a negative number is undefined.");
        return std::sqrt(value);
    }

    // Modulus
    static int modulus(int a, int b) {
        if (b == 0) throw std::invalid_argument("Modulus by zero is undefined.");
        return a % b;
    }

    // Absolute Value
    static double absolute(double value) {
        return std::abs(value);
    }

    // Rounding
    static double round(double value) {
        return std::round(value);
    }

    // Ceiling
    static double ceil(double value) {
        return std::ceil(value);
    }

    // Floor
    static double floor(double value) {
        return std::floor(value);
    }

    // Factorial
    static long long factorial(int n) {
        if (n < 0) throw std::invalid_argument("Factorial of a negative number is undefined.");
        long long result = 1;
        for (int i = 2; i <= n; ++i) {
            result *= i;
        }
        return result;
    }
};
