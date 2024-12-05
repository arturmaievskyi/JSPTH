package main

import (
	"fmt"
)

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