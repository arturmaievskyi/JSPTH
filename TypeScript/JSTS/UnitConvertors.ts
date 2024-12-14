// File: UnitConverters.ts

export class UnitConverters {
    // Storage Converter: Bytes, Kilobytes, Megabytes, etc.
    static storageConverter(value: number, fromUnit: string, toUnit: string): number {
        const units = ["B", "KB", "MB", "GB", "TB", "PB"];
        const fromIndex = units.indexOf(fromUnit.toUpperCase());
        const toIndex = units.indexOf(toUnit.toUpperCase());
        if (fromIndex === -1 || toIndex === -1) throw new Error("Invalid storage unit");
        return value * 1024 ** (fromIndex - toIndex);
    }

    // Area Converter: Square meters, square kilometers, etc.
    static areaConverter(value: number, fromUnit: string, toUnit: string): number {
        const units: Record<string, number> = {
            "m²": 1,
            "km²": 1e6,
            "cm²": 0.0001,
            "mm²": 0.000001,
            "ft²": 0.092903,
            "in²": 0.00064516,
            "acre": 4046.86,
        };
        if (!units[fromUnit] || !units[toUnit]) throw new Error("Invalid area unit");
        return (value * units[fromUnit]) / units[toUnit];
    }

    // Volume Converter: Cubic meters, liters, milliliters, etc.
    static volumeConverter(value: number, fromUnit: string, toUnit: string): number {
        const units: Record<string, number> = {
            "m³": 1,
            "l": 0.001,
            "ml": 0.000001,
            "cm³": 0.000001,
            "ft³": 0.0283168,
            "in³": 0.0000163871,
            "gallon": 0.00378541,
        };
        if (!units[fromUnit] || !units[toUnit]) throw new Error("Invalid volume unit");
        return (value * units[fromUnit]) / units[toUnit];
    }

    // Speed Converter: Meters per second, kilometers per hour, miles per hour
    static speedConverter(value: number, fromUnit: string, toUnit: string): number {
        const units: Record<string, number> = {
            "m/s": 1,
            "km/h": 1 / 3.6,
            "mph": 0.44704,
            "ft/s": 0.3048,
            "knot": 0.514444,
        };
        if (!units[fromUnit] || !units[toUnit]) throw new Error("Invalid speed unit");
        return (value * units[fromUnit]) / units[toUnit];
    }

    // Mass Converter: Kilograms, grams, pounds, etc.
    static massConverter(value: number, fromUnit: string, toUnit: string): number {
        const units: Record<string, number> = {
            "kg": 1,
            "g": 0.001,
            "mg": 0.000001,
            "lb": 0.453592,
            "oz": 0.0283495,
            "tonne": 1000,
        };
        if (!units[fromUnit] || !units[toUnit]) throw new Error("Invalid mass unit");
        return (value * units[fromUnit]) / units[toUnit];
    }

    // Distance Converter: Meters, kilometers, miles, etc.
    static distanceConverter(value: number, fromUnit: string, toUnit: string): number {
        const units: Record<string, number> = {
            "m": 1,
            "km": 1000,
            "cm": 0.01,
            "mm": 0.001,
            "mile": 1609.34,
            "yard": 0.9144,
            "ft": 0.3048,
            "in": 0.0254,
        };
        if (!units[fromUnit] || !units[toUnit]) throw new Error("Invalid distance unit");
        return (value * units[fromUnit]) / units[toUnit];
    }

    // Temperature Converter: Celsius, Fahrenheit, Kelvin
    static temperatureConverter(value: number, fromUnit: string, toUnit: string): number {
        if (fromUnit === "C" && toUnit === "F") return value * 1.8 + 32;
        if (fromUnit === "F" && toUnit === "C") return (value - 32) / 1.8;
        if (fromUnit === "C" && toUnit === "K") return value + 273.15;
        if (fromUnit === "K" && toUnit === "C") return value - 273.15;
        if (fromUnit === "F" && toUnit === "K") return ((value - 32) / 1.8) + 273.15;
        if (fromUnit === "K" && toUnit === "F") return (value - 273.15) * 1.8 + 32;
        if (fromUnit === toUnit) return value;
        throw new Error("Invalid temperature conversion");
    }

    // Other converters (for brevity, similar patterns can be followed for the others)
    // PressureConverter, EnergyConverter, FrequencyConverter, etc.
    // Follow a similar pattern with `Record<string, number>` for constants.

    // Example: Pressure Converter
    static pressureConverter(value: number, fromUnit: string, toUnit: string): number {
        const units: Record<string, number> = {
            "Pa": 1,
            "atm": 101325,
            "bar": 100000,
            "psi": 6894.76,
            "mmHg": 133.322,
        };
        if (!units[fromUnit] || !units[toUnit]) throw new Error("Invalid pressure unit");
        return (value * units[fromUnit]) / units[toUnit];
    }
}
