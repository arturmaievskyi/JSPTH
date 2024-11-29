package mathmain

import (
	"math"
)

// Trigonometry provides various trigonometric and related functions.
type Trigonometry struct{}

// Sine returns the sine of an angle (in radians).
func (Trigonometry) Sine(angle float64) float64 {
	return math.Sin(angle)
}

// Cosine returns the cosine of an angle (in radians).
func (Trigonometry) Cosine(angle float64) float64 {
	return math.Cos(angle)
}

// Tangent returns the tangent of an angle (in radians).
func (Trigonometry) Tangent(angle float64) float64 {
	return math.Tan(angle)
}

// ArcSine returns the arcsine (inverse sine) of a value.
func (Trigonometry) ArcSine(value float64) float64 {
	return math.Asin(value)
}

// ArcCosine returns the arccosine (inverse cosine) of a value.
func (Trigonometry) ArcCosine(value float64) float64 {
	return math.Acos(value)
}

// ArcTangent returns the arctangent (inverse tangent) of a value.
func (Trigonometry) ArcTangent(value float64) float64 {
	return math.Atan(value)
}

// LawOfCosines calculates the third side of a triangle given two sides and the included angle.
func (Trigonometry) LawOfCosines(a, b, angle float64) float64 {
	return math.Sqrt(a*a + b*b - 2*a*b*math.Cos(angle))
}

// LawOfSines calculates a side length using the law of sines.
func (Trigonometry) LawOfSines(a, A, B float64) float64 {
	return (a * math.Sin(B)) / math.Sin(A)
}

// Secant returns the secant of an angle (in radians).
func (Trigonometry) Secant(angle float64) float64 {
	return 1 / math.Cos(angle)
}

// Cosecant returns the cosecant of an angle (in radians).
func (Trigonometry) Cosecant(angle float64) float64 {
	return 1 / math.Sin(angle)
}

// Cotangent returns the cotangent of an angle (in radians).
func (Trigonometry) Cotangent(angle float64) float64 {
	return 1 / math.Tan(angle)
}

// SineSum calculates the sine of the sum of two angles.
func (Trigonometry) SineSum(a, b float64) float64 {
	return math.Sin(a)*math.Cos(b) + math.Cos(a)*math.Sin(b)
}

// CosineSum calculates the cosine of the sum of two angles.
func (Trigonometry) CosineSum(a, b float64) float64 {
	return math.Cos(a)*math.Cos(b) - math.Sin(a)*math.Sin(b)
}

// TangentSum calculates the tangent of the sum of two angles.
func (Trigonometry) TangentSum(a, b float64) float64 {
	return (math.Tan(a) + math.Tan(b)) / (1 - math.Tan(a)*math.Tan(b))
}

// SineDouble calculates the sine of twice an angle.
func (Trigonometry) SineDouble(a float64) float64 {
	return 2 * math.Sin(a) * math.Cos(a)
}

// CosineDouble calculates the cosine of twice an angle.
func (Trigonometry) CosineDouble(a float64) float64 {
	return math.Cos(a)*math.Cos(a) - math.Sin(a)*math.Sin(a)
}

// TangentDouble calculates the tangent of twice an angle.
func (Trigonometry) TangentDouble(a float64) float64 {
	return 2 * math.Tan(a) / (1 - math.Tan(a)*math.Tan(a))
}

// PolarToCartesian converts polar coordinates to Cartesian coordinates.
func (Trigonometry) PolarToCartesian(r, theta float64) (x, y float64) {
	x = r * math.Cos(theta)
	y = r * math.Sin(theta)
	return x, y
}