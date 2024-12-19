package JSGo

import (
	"errors"
	"math"
	"fmt"
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


// Converters provides various unit conversion utilities.
type Converters struct{}

// StorageConverter converts between different storage units.
func (Converters) StorageConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"bytes":      1,
		"kilobytes":  1024,
		"megabytes":  1024 * 1024,
		"gigabytes":  1024 * 1024 * 1024,
		"terabytes":  1024 * 1024 * 1024 * 1024,
		"petabytes":  1024 * 1024 * 1024 * 1024 * 1024,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// AreaConverter converts between different area units.
func (Converters) AreaConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"square_meter":  1,
		"square_kilometer":  1_000_000,
		"hectare":       10_000,
		"acre":          4046.8564224,
		"square_foot":   0.092903,
		"square_yard":   0.83612736,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// VolumeConverter converts between different volume units.
func (Converters) VolumeConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"liter":       1,
		"milliliter":  0.001,
		"cubic_meter": 1000,
		"gallon":      3.78541,
		"quart":       0.946353,
		"pint":        0.473176,
		"cubic_inch":  0.0163871,
		"cubic_foot":  28.3168,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// SpeedConverter converts between different speed units.
func (Converters) SpeedConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"meters_per_second": 1,
		"kilometers_per_hour":  1 / 3.6,
		"miles_per_hour":    1 / 2.237,
		"knots":             1 / 1.944,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// MassConverter converts between different mass units.
func (Converters) MassConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"kilogram":  1,
		"gram":      0.001,
		"milligram": 0.000001,
		"tonne":     1000,
		"pound":     0.453592,
		"ounce":     0.0283495,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}
func (Converters) DistanceConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"meters":     1,
		"kilometers": 1000,
		"miles":      1609.34,
		"yards":      0.9144,
		"feet":       0.3048,
		"inches":     0.0254,
		"nautical_miles": 1852,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// TemperatureConverter converts between different temperature scales.
func (Converters) TemperatureConverter(value float64, from, to string) (float64, error) {
	switch from {
	case "celsius":
		if to == "fahrenheit" {
			return value*9/5 + 32, nil
		} else if to == "kelvin" {
			return value + 273.15, nil
		}
	case "fahrenheit":
		if to == "celsius" {
			return (value - 32) * 5 / 9, nil
		} else if to == "kelvin" {
			return (value-32)*5/9 + 273.15, nil
		}
	case "kelvin":
		if to == "celsius" {
			return value - 273.15, nil
		} else if to == "fahrenheit" {
			return (value-273.15)*9/5 + 32, nil
		}
	}
	return 0, errors.New("invalid temperature conversion")
}

// PressureConverter converts between different pressure units.
func (Converters) PressureConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"pascal":       1,
		"kilopascal":   1000,
		"bar":          100000,
		"psi":          6894.76,
		"atmosphere":   101325,
		"millibar":     100,
		"torr":         133.322,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// EnergyConverter converts between different energy units.
func (Converters) EnergyConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"joules":      1,
		"kilojoules":  1000,
		"calories":    4.184,
		"kilocalories": 4184,
		"watt_hours":  3600,
		"kilowatt_hours": 3600000,
		"electron_volts": 1.60218e-19,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// FrequencyConverter converts between different frequency units.
func (Converters) FrequencyConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"hertz":        1,
		"kilohertz":    1000,
		"megahertz":    1e6,
		"gigahertz":    1e9,
		"terahertz":    1e12,
		"revolutions_per_minute": 1 / 60,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}
func (Converters) PowerConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"watts":          1,
		"kilowatts":      1000,
		"horsepower":     745.7,
		"btus_per_hour":  0.293071,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// ForceConverter converts between different force units.
func (Converters) ForceConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"newton":        1,
		"kilonewton":    1000,
		"pound_force":   4.44822,
		"dyne":          0.00001,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// TorqueConverter converts between different torque units.
func (Converters) TorqueConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"newton_meter":       1,
		"kilonewton_meter":   1000,
		"foot_pound":         1.35582,
		"inch_pound":         0.112985,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// DensityConverter converts between different density units.
func (Converters) DensityConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"kilogram_per_cubic_meter": 1,
		"gram_per_cubic_centimeter": 1000,
		"pound_per_cubic_foot":     16.0185,
		"ounce_per_cubic_inch":     1729.99,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// LuminanceConverter converts between different luminance units.
func (Converters) LuminanceConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"candela_per_square_meter": 1,
		"candela_per_square_foot":  10.764,
		"nit":                      1,
		"footlambert":              3.426259,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}
func (Converters) FuelEfficiencyConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"miles_per_gallon":          1,
		"kilometers_per_liter":      2.35215,
		"liters_per_100_kilometers": 235.215,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// RadioactivityConverter converts between different radioactivity units.
func (Converters) RadioactivityConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"becquerel":      1,
		"curie":          3.7e10,
		"rutherford":     1e6,
		"disintegrations_per_second": 1,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// DataTransferRateConverter converts between different data transfer rate units.
func (Converters) DataTransferRateConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"bps":       1,
		"Kbps":      1e3,
		"Mbps":      1e6,
		"Gbps":      1e9,
		"Tbps":      1e12,
		"Bytes_per_second": 8,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// CapacitanceConverter converts between different capacitance units.
func (Converters) CapacitanceConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"farad":       1,
		"millifarad":  0.001,
		"microfarad":  0.000001,
		"nanofarad":   0.000000001,
		"picofarad":   0.000000000001,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// IlluminationIntensityConverter converts between different illumination intensity units.
func (Converters) IlluminationIntensityConverter(value float64, from, to string) (float64, error) {
	units := map[string]float64{
		"lux":        1,
		"foot_candle": 10.764,
		"phot":       10000,
	}
	fromFactor, ok1 := units[from]
	toFactor, ok2 := units[to]
	if !ok1 || !ok2 {
		return 0, fmt.Errorf("invalid units: %s or %s", from, to)
	}
	return value * fromFactor / toFactor, nil
}

// Main function to demonstrate usage.
func main() {
	converter := Converters{}

	// Fuel Efficiency Conversion Example
	fuelEfficiency, err := converter.FuelEfficiencyConverter(1, "miles_per_gallon", "kilometers_per_liter")
	if err == nil {
		fmt.Println("Fuel Efficiency Conversion (1 mpg to km/l):", fuelEfficiency)
	} else {
		fmt.Println("FuelEfficiencyConverter Error:", err)
	}

	// Radioactivity Conversion Example
	radioactivity, err := converter.RadioactivityConverter(1, "curie", "becquerel")
	if err == nil {
		fmt.Println("Radioactivity Conversion (1 curie to becquerel):", radioactivity)
	} else {
		fmt.Println("RadioactivityConverter Error:", err)
	}

	// Data Transfer Rate Conversion Example
	dataRate, err := converter.DataTransferRateConverter(1, "Gbps", "Mbps")
	if err == nil {
		fmt.Println("Data Transfer Rate Conversion (1 Gbps to Mbps):", dataRate)
	} else {
		fmt.Println("DataTransferRateConverter Error:", err)
	}

	// Capacitance Conversion Example
	capacitance, err := converter.CapacitanceConverter(1, "farad", "microfarad")
	if err == nil {
		fmt.Println("Capacitance Conversion (1 farad to microfarad):", capacitance)
	} else {
		fmt.Println("CapacitanceConverter Error:", err)
	}

	// Illumination Intensity Conversion Example
	illumination, err := converter.IlluminationIntensityConverter(1, "lux", "foot_candle")
	if err == nil {
		fmt.Println("Illumination Intensity Conversion (1 lux to foot-candles):", illumination)
	} else {
		fmt.Println("IlluminationIntensityConverter Error:", err)
	}
}
