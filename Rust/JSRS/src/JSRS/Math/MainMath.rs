struct Math;
use std::f64;

impl Math {
    fn add(a: f64, b: f64) -> f64 {
        a + b
    }

    fn subtract(a: f64, b: f64) -> f64 {
        a - b
    }

    fn multiply(a: f64, b: f64) -> f64 {
        a * b
    }

    fn divide(a: f64, b: f64) -> Result<f64, &'static str> {
        if b == 0.0 {
            Err("Cannot divide by zero")
        } else {
            Ok(a / b)
        }
    }
}

/// A MathSolver class for various mathematical computations.
struct MathSolver;

impl MathSolver {
    /// Solves a quadratic equation of the form ax^2 + bx + c = 0.
    fn quadratic_solver(a: f64, b: f64, c: f64) -> Result<(f64, f64), &'static str> {
        if a == 0.0 {
            return Err("Coefficient 'a' cannot be zero in a quadratic equation.");
        }
        let discriminant = b * b - 4.0 * a * c;
        if discriminant < 0.0 {
            return Err("No real roots.");
        }
        let root1 = (-b + discriminant.sqrt()) / (2.0 * a);
        let root2 = (-b - discriminant.sqrt()) / (2.0 * a);
        Ok((root1, root2))
    }

    /// Solves a linear equation of the form ax + b = 0.
    fn linear_solver(a: f64, b: f64) -> Result<f64, &'static str> {
        if a == 0.0 {
            return Err("Coefficient 'a' cannot be zero in a linear equation.");
        }
        Ok(-b / a)
    }

    /// Computes the value of an exponential equation y = a^x.
    fn exponential_solver(base: f64, exponent: f64) -> f64 {
        base.powf(exponent)
    }

    /// Computes the logarithm of a number with a given base.
    fn logarithm_solver(value: f64, base: f64) -> Result<f64, &'static str> {
        if value <= 0.0 || base <= 0.0 || base == 1.0 {
            return Err("Logarithm arguments must be positive, and the base cannot be 1.");
        }
        Ok(value.log(base))
    }

    /// Evaluates a polynomial at a given x value.
    fn polynomial_eval(coefficients: &[f64], x: f64) -> f64 {
        coefficients.iter().rev().fold(0.0, |acc, &coeff| acc * x + coeff)
    }

    /// Computes the greatest common divisor (GCD) of two integers.
    fn gcd(a: i64, b: i64) -> i64 {
        if b == 0 {
            a.abs()
        } else {
            MathSolver::gcd(b, a % b)
        }
    }

    /// Computes the least common multiple (LCM) of two integers.
    fn lcm(a: i64, b: i64) -> i64 {
        (a * b).abs() / MathSolver::gcd(a, b)
    }

    /// Computes the binomial coefficient "n choose k".
    fn binomial_coefficient(n: u64, k: u64) -> u64 {
        if k > n {
            return 0;
        }
        (0..k).fold(1, |acc, i| acc * (n - i) / (i + 1))
    }

    /// Computes the nth term of an arithmetic progression.
    fn arithmetic_progression(a: f64, d: f64, n: u64) -> f64 {
        a + (n as f64 - 1.0) * d
    }

    /// Computes the nth term of a geometric progression.
    fn geometric_progression(a: f64, r: f64, n: u64) -> f64 {
        a * r.powf((n as f64 - 1.0))
    }

    /// Computes the sum of the first n terms of a geometric series.
    fn geometric_series_sum(a: f64, r: f64, n: u64) -> Result<f64, &'static str> {
        if r == 1.0 {
            Ok(a * n as f64)
        } else {
            Ok(a * (1.0 - r.powf(n as f64)) / (1.0 - r))
        }
    }
}