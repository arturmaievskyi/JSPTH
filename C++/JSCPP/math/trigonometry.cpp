#include <cmath>
#include <utility> // for std::pair
#include <stdexcept> // for std::invalid_argument

class Trigonometry {
public:
    // Basic Trigonometric Functions
    static double sine(double angle) {
        return std::sin(angle);
    }

    static double cosine(double angle) {
        return std::cos(angle);
    }

    static double tangent(double angle) {
        if (std::cos(angle) == 0) throw std::invalid_argument("Tangent undefined for this angle.");
        return std::tan(angle);
    }

    static double secant(double angle) {
        if (std::cos(angle) == 0) throw std::invalid_argument("Secant undefined for this angle.");
        return 1.0 / std::cos(angle);
    }

    static double cosecant(double angle) {
        if (std::sin(angle) == 0) throw std::invalid_argument("Cosecant undefined for this angle.");
        return 1.0 / std::sin(angle);
    }

    static double cotangent(double angle) {
        if (std::sin(angle) == 0) throw std::invalid_argument("Cotangent undefined for this angle.");
        return 1.0 / std::tan(angle);
    }

    // Inverse Trigonometric Functions
    static double arcsine(double value) {
        if (value < -1.0 || value > 1.0) throw std::invalid_argument("Input out of domain for arcsine.");
        return std::asin(value);
    }

    static double arccosine(double value) {
        if (value < -1.0 || value > 1.0) throw std::invalid_argument("Input out of domain for arccosine.");
        return std::acos(value);
    }

    static double arctangent(double value) {
        return std::atan(value);
    }

    // Law of Cosines
    static double law_of_cosines(double a, double b, double angle) {
        return std::sqrt(a * a + b * b - 2 * a * b * std::cos(angle));
    }

    // Law of Sines
    static double law_of_sines(double a, double A, double B) {
        if (std::sin(A) == 0) throw std::invalid_argument("Division by zero in law of sines.");
        return a * std::sin(B) / std::sin(A);
    }

    // Trigonometric Identities
    static double sine_sum(double angle1, double angle2) {
        return std::sin(angle1) * std::cos(angle2) + std::cos(angle1) * std::sin(angle2);
    }

    static double cosine_sum(double angle1, double angle2) {
        return std::cos(angle1) * std::cos(angle2) - std::sin(angle1) * std::sin(angle2);
    }

    static double tangent_sum(double angle1, double angle2) {
        double denom = 1 - std::tan(angle1) * std::tan(angle2);
        if (denom == 0) throw std::invalid_argument("Tangent sum undefined.");
        return (std::tan(angle1) + std::tan(angle2)) / denom;
    }

    static double sine_double(double angle) {
        return 2 * std::sin(angle) * std::cos(angle);
    }

    static double cosine_double(double angle) {
        return std::cos(angle) * std::cos(angle) - std::sin(angle) * std::sin(angle);
    }

    static double tangent_double(double angle) {
        double denom = 1 - std::tan(angle) * std::tan(angle);
        if (denom == 0) throw std::invalid_argument("Tangent double angle undefined.");
        return 2 * std::tan(angle) / denom;
    }

    // Coordinate Conversion
    static std::pair<double, double> polar_to_cartesian(double radius, double angle) {
        double x = radius * std::cos(angle);
        double y = radius * std::sin(angle);
        return {x, y};
    }

    static std::pair<double, double> cartesian_to_polar(double x, double y) {
        double radius = std::sqrt(x * x + y * y);
        double angle = std::atan2(y, x);
        return {radius, angle};
    }
};
