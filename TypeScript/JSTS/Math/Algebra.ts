// File: MathUtils.ts

export class Algebra {
    // Quadratic Equation Solver: ax^2 + bx + c = 0
    static quadraticSolver(a: number, b: number, c: number): [number, number] | string {
        const discriminant = b ** 2 - 4 * a * c;
        if (discriminant < 0) {
            return "No real roots";
        }
        const root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        const root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        return [root1, root2];
    }

    // Linear Equation Solver: ax + b = 0
    static linearSolver(a: number, b: number): number {
        if (a === 0) {
            throw new Error("No solution (a = 0)");
        }
        return -b / a;
    }

    // Exponential Solver: a^x = b
    static exponentialSolver(a: number, b: number): number {
        if (a <= 0 || b <= 0) {
            throw new Error("Base and result must be positive");
        }
        return Math.log(b) / Math.log(a);
    }

    // Logarithm Solver: log_a(b)
    static logarithmSolver(a: number, b: number): number {
        if (a <= 0 || a === 1 || b <= 0) {
            throw new Error("Invalid base or input");
        }
        return Math.log(b) / Math.log(a);
    }

    // Polynomial Evaluation: Given coefficients [a_n, a_(n-1), ..., a_0], calculate P(x)
    static polynomialEval(coefficients: number[], x: number): number {
        return coefficients.reduce((result, coeff, index) => {
            return result + coeff * x ** (coefficients.length - index - 1);
        }, 0);
    }

    // Greatest Common Divisor (GCD) using Euclidean algorithm
    static gcd(a: number, b: number): number {
        while (b !== 0) {
            [a, b] = [b, a % b];
        }
        return Math.abs(a);
    }

    // Least Common Multiple (LCM)
    static lcm(a: number, b: number): number {
        return Math.abs(a * b) / Algebra.gcd(a, b);
    }

    // Binomial Coefficient: C(n, k)
    static binomialCoefficient(n: number, k: number): number {
        if (k < 0 || k > n) {
            return 0;
        }
        if (k === 0 || k === n) {
            return 1;
        }
        let result = 1;
        for (let i = 1; i <= k; i++) {
            result = (result * (n - i + 1)) / i;
        }
        return result;
    }

    // Arithmetic Progression: Sum of AP (a, a+d, a+2d, ..., a+(n-1)d)
    static arithmeticProgression(a: number, d: number, n: number): number {
        return (n / 2) * (2 * a + (n - 1) * d);
    }

    // Geometric Progression: Sum of GP (a, ar, ar^2, ..., ar^(n-1))
    static geometricProgression(a: number, r: number, n: number): number {
        if (r === 1) {
            return a * n;
        }
        return a * (1 - r ** n) / (1 - r);
    }

    // Geometric Series Sum: Infinite series (a, ar, ar^2, ...)
    static geometricSeriesSum(a: number, r: number): number {
        if (Math.abs(r) >= 1) {
            throw new Error("Infinite series does not converge for |r| >= 1");
        }
        return a / (1 - r);
    }
}
