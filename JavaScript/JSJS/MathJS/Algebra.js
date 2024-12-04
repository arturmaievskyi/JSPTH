class MathUtils {
    constructor() {}
  
    // Quadratic Equation Solver: ax^2 + bx + c = 0
    quadratic_solver(a, b, c) {
        const discriminant = b ** 2 - 4 * a * c;
        if (discriminant < 0) return null; // No real roots
        const root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        const root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        return [root1, root2];
    }
  
    // Linear Equation Solver: ax + b = 0
    linear_solver(a, b) {
        if (a === 0) throw new Error("No solution; 'a' cannot be zero.");
        return -b / a;
    }
  
    // Exponential Equation Solver: a * b^x = c
    exponential_solver(a, b, c) {
        if (a === 0 || b <= 0) throw new Error("Invalid parameters.");
        const x = Math.log(c / a) / Math.log(b);
        return x;
    }
  
    // Logarithmic Equation Solver: log_b(x) = y
    logarithm_solver(base, x) {
        if (base <= 0 || base === 1 || x <= 0) throw new Error("Invalid parameters.");
        return Math.log(x) / Math.log(base);
    }
  
    // Polynomial Evaluation: P(x) = a_n * x^n + ... + a_1 * x + a_0
    polynomial_eval(coefficients, x) {
        return coefficients.reduce((acc, coef, index) => acc + coef * x ** (coefficients.length - index - 1), 0);
    }
  
    // Greatest Common Divisor (GCD)
    gcd(a, b) {
        while (b !== 0) {
            [a, b] = [b, a % b];
        }
        return Math.abs(a);
    }
  
    // Least Common Multiple (LCM)
    lcm(a, b) {
        return (Math.abs(a * b) / this.gcd(a, b));
    }
  
    // Binomial Coefficient: C(n, k) = n! / (k! * (n - k)!)
    binomial_coefficient(n, k) {
        if (k > n || n < 0 || k < 0) throw new Error("Invalid parameters.");
        const factorial = (num) => (num === 0 ? 1 : num * factorial(num - 1));
        return factorial(n) / (factorial(k) * factorial(n - k));
    }
  
    // Arithmetic Progression (AP): a_n = a + (n - 1) * d
    arithmetic_progression(a, d, n) {
        return a + (n - 1) * d;
    }
  
    // Geometric Progression (GP): a_n = a * r^(n - 1)
    geometric_progression(a, r, n) {
        return a * r ** (n - 1);
    }
  
    // Geometric Series Sum: S_n = a * (1 - r^n) / (1 - r) if r != 1
    geometric_series_sum(a, r, n) {
        if (r === 1) return a * n;
        return (a * (1 - r ** n)) / (1 - r);
    }
}
  