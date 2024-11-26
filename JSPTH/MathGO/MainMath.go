// File: math.go
package main

import (
	"errors"
	"fmt"
	"log"
	"math"
)

// MathOperations provides various mathematical functions.
type MathOperations struct{}

// Add returns the sum of two numbers.
func (MathOperations) Add(a, b float64) float64 {
	return a + b
}

// Subtract returns the difference of two numbers.
func (MathOperations) Subtract(a, b float64) float64 {
	return a - b
}

// Multiply returns the product of two numbers.
func (MathOperations) Multiply(a, b float64) float64 {
	return a * b
}

// Divide performs division and returns the result. Returns an error if division by zero occurs.
func (MathOperations) Divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("division by zero is not allowed")
	}
	return a / b, nil
}

// Factorial returns the factorial of an integer. Returns an error for negative numbers.
func (MathOperations) Factorial(n int) (int, error) {
	if n < 0 {
		return 0, errors.New("factorial is not defined for negative numbers")
	}
	result := 1
	for i := 2; i <= n; i++ {
		result *= i
	}
	return result, nil
}

// Power returns the result of raising base to the power exponent.
func (MathOperations) Power(base, exponent float64) float64 {
	return math.Pow(base, exponent)
}

// IsPrime checks if a number is prime.
func (MathOperations) IsPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
