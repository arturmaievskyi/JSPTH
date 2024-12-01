#include <iostream>
#include <vector>
#include <cmath>
#include <stdexcept>

class MathUtils {
public:
    // Solves ax^2 + bx + c = 0
    static std::pair<double, double> quadratic_solver(double a, double b, double c) {
        if (a == 0) throw std::invalid_argument("Coefficient 'a' cannot be zero for a quadratic equation.");
        double discriminant = b * b - 4 * a * c;
        if (discriminant < 0) throw std::invalid_argument("No real roots.");
        double root1 = (-b + std::sqrt(discriminant)) / (2 * a);
        double root2 = (-b - std::sqrt(discriminant)) / (2 * a);
        return {root1, root2};
    }

    // Solves ax + b = 0
    static double linear_solver(double a, double b) {
        if (a == 0) throw std::invalid_argument("Coefficient 'a' cannot be zero for a linear equation.");
        return -b / a;
    }

    // Solves a * e^(bx) = c
    static double exponential_solver(double a, double b, double c) {
        if (a == 0 || c <= 0) throw std::invalid_argument("Invalid arguments for exponential equation.");
        return std::log(c / a) / b;
    }

    // Solves log_b(x) = c
    static double logarithm_solver(double base, double x) {
        if (base <= 0 || base == 1 || x <= 0) throw std::invalid_argument("Invalid arguments for logarithm.");
        return std::log(x) / std::log(base);
    }

    // Evaluates a polynomial at a given x
    static double polynomial_eval(const std::vector<double>& coefficients, double x) {
        double result = 0;
        for (size_t i = 0; i < coefficients.size(); ++i) {
            result += coefficients[i] * std::pow(x, i);
        }
        return result;
    }

    // Greatest Common Divisor
    static int gcd(int a, int b) {
        return b == 0 ? std::abs(a) : gcd(b, a % b);
    }

    // Least Common Multiple
    static int lcm(int a, int b) {
        if (a == 0 || b == 0) throw std::invalid_argument("LCM undefined for zero.");
        return std::abs(a * b) / gcd(a, b);
    }

    // Binomial Coefficient (n choose k)
    static long long binomial_coefficient(int n, int k) {
        if (k < 0 || k > n) throw std::invalid_argument("Invalid arguments for binomial coefficient.");
        if (k == 0 || k == n) return 1;
        long long result = 1;
        for (int i = 1; i <= k; ++i) {
            result *= (n - i + 1);
            result /= i;
        }
        return result;
    }

    // Arithmetic Progression nth term
    static double arithmetic_progression(double a, double d, int n) {
        return a + (n - 1) * d;
    }

    // Geometric Progression nth term
    static double geometric_progression(double a, double r, int n) {
        return a * std::pow(r, n - 1);
    }

    // Geometric Series Sum
    static double geometric_series_sum(double a, double r, int n) {
        if (r == 1) return a * n;
        return a * (1 - std::pow(r, n)) / (1 - r);
    }
};

