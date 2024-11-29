package mathmain

import (
	"errors"
	"math"
)

// Mathematics provides various mathematical functions.
type Mathematics struct{}

// QuadraticSolver solves a quadratic equation ax^2 + bx + c = 0.
// Returns the roots or an error if no real roots exist.
func (Mathematics) QuadraticSolver(a, b, c float64) (float64, float64, error) {
	discriminant := b*b - 4*a*c
	if discriminant < 0 {
		return 0, 0, errors.New("no real roots")
	}
	root1 := (-b + math.Sqrt(discriminant)) / (2 * a)
	root2 := (-b - math.Sqrt(discriminant)) / (2 * a)
	return root1, root2, nil
}

// LinearSolver solves a linear equation ax + b = 0.
// Returns the solution or an error if a = 0.
func (Mathematics) LinearSolver(a, b float64) (float64, error) {
	if a == 0 {
		return 0, errors.New("no solution for a = 0")
	}
	return -b / a, nil
}

// ExponentialSolver solves an equation of the form a^x = b.
// Returns x or an error if a <= 0 or b <= 0.
func (Mathematics) ExponentialSolver(a, b float64) (float64, error) {
	if a <= 0 || b <= 0 {
		return 0, errors.New("base and result must be positive")
	}
	return math.Log(b) / math.Log(a), nil
}

// LogarithmSolver solves a logarithmic equation log_a(x) = b.
// Returns x or an error if a <= 0 or b <= 0.
func (Mathematics) LogarithmSolver(a, b float64) (float64, error) {
	if a <= 0 || b <= 0 {
		return 0, errors.New("base and result must be positive")
	}
	return math.Pow(a, b), nil
}

// PolynomialEval evaluates a polynomial at a given x.
// Coefficients are given in decreasing order of powers.
func (Mathematics) PolynomialEval(coeffs []float64, x float64) float64 {
	result := 0.0
	for i, coef := range coeffs {
		power := len(coeffs) - i - 1
		result += coef * math.Pow(x, float64(power))
	}
	return result
}

// GCD calculates the greatest common divisor of two integers.
func (Mathematics) GCD(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// LCM calculates the least common multiple of two integers.
func (Mathematics) LCM(a, b int) int {
	return a * b / Mathematics{}.GCD(a, b)
}

// BinomialCoefficient calculates the binomial coefficient C(n, k).
func (Mathematics) BinomialCoefficient(n, k int) int {
	if k > n || k < 0 {
		return 0
	}
	result := 1
	for i := 0; i < k; i++ {
		result = result * (n - i) / (i + 1)
	}
	return result
}

// ArithmeticProgression calculates the nth term of an AP.
func (Mathematics) ArithmeticProgression(a, d, n int) int {
	return a + (n-1)*d
}

// GeometricProgression calculates the nth term of a GP.
func (Mathematics) GeometricProgression(a, r, n int) int {
	return a * int(math.Pow(float64(r), float64(n-1)))
}

// GeometricSeriesSum calculates the sum of the first n terms of a GP.
func (Mathematics) GeometricSeriesSum(a, r, n int) int {
	if r == 1 {
		return a * n
	}
	return int(float64(a) * (1 - math.Pow(float64(r), float64(n))) / (1 - float64(r)))
}