class UnitConverter {
    constructor() {}
  
    // Storage Converter
    storageConverter(value, fromUnit, toUnit) {
        const units = { B: 1, KB: 1024, MB: 1024 ** 2, GB: 1024 ** 3, TB: 1024 ** 4 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Area Converter
    areaConverter(value, fromUnit, toUnit) {
        const units = { sqm: 1, sqkm: 1e6, sqft: 0.092903, sqyd: 0.836127, acre: 4046.85642 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Volume Converter
    volumeConverter(value, fromUnit, toUnit) {
        const units = { cubicm: 1, liter: 0.001, ml: 1e-6, cubicft: 0.0283168, gallon: 0.00378541 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Speed Converter
    speedConverter(value, fromUnit, toUnit) {
        const units = { 'm/s': 1, 'km/h': 1 / 3.6, 'mph': 0.44704, 'knot': 0.514444 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Mass Converter
    massConverter(value, fromUnit, toUnit) {
        const units = { g: 1, kg: 1000, lb: 453.592, oz: 28.3495, ton: 1e6 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Distance Converter
    distanceConverter(value, fromUnit, toUnit) {
        const units = { m: 1, km: 1000, mile: 1609.34, yard: 0.9144, ft: 0.3048, inch: 0.0254 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Temperature Converter
    temperatureConverter(value, fromUnit, toUnit) {
        if (fromUnit === 'C' && toUnit === 'F') return value * 1.8 + 32;
        if (fromUnit === 'C' && toUnit === 'K') return value + 273.15;
        if (fromUnit === 'F' && toUnit === 'C') return (value - 32) / 1.8;
        if (fromUnit === 'F' && toUnit === 'K') return ((value - 32) / 1.8) + 273.15;
        if (fromUnit === 'K' && toUnit === 'C') return value - 273.15;
        if (fromUnit === 'K' && toUnit === 'F') return (value - 273.15) * 1.8 + 32;
        if (fromUnit === toUnit) return value;
    }
  
    // Pressure Converter
    pressureConverter(value, fromUnit, toUnit) {
        const units = { Pa: 1, kPa: 1000, atm: 101325, psi: 6894.76, bar: 100000 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Energy Converter
    energyConverter(value, fromUnit, toUnit) {
        const units = { J: 1, kJ: 1000, cal: 4.184, kcal: 4184, Wh: 3600, kWh: 3.6e6 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Frequency Converter
    frequencyConverter(value, fromUnit, toUnit) {
        const units = { Hz: 1, kHz: 1e3, MHz: 1e6, GHz: 1e9 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Power Converter
    powerConverter(value, fromUnit, toUnit) {
        const units = { W: 1, kW: 1000, hp: 745.7 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Force Converter
    forceConverter(value, fromUnit, toUnit) {
        const units = { N: 1, kN: 1000, lbf: 4.44822, dyne: 1e-5 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Torque Converter
    torqueConverter(value, fromUnit, toUnit) {
        const units = { Nm: 1, lbft: 1.35582 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Density Converter
    densityConverter(value, fromUnit, toUnit) {
        const units = { 'kg/m3': 1, 'g/cm3': 1000, 'lb/ft3': 16.0185 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Luminance Converter
    luminanceConverter(value, fromUnit, toUnit) {
        const units = { cd_m2: 1, nit: 1, ftL: 3.4262591 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Fuel Efficiency Converter
    fuelEfficiencyConverter(value, fromUnit, toUnit) {
        const units = { 'km/l': 1, 'mpg': 0.425144, 'l/100km': 100 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Radioactivity Converter
    radioactivityConverter(value, fromUnit, toUnit) {
        const units = { Bq: 1, Ci: 3.7e10 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Data Transfer Rate Converter
    dataTransferRateConverter(value, fromUnit, toUnit) {
        const units = { bps: 1, kbps: 1e3, Mbps: 1e6, Gbps: 1e9 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Capacitance Converter
    capacitanceConverter(value, fromUnit, toUnit) {
        const units = { F: 1, mF: 1e-3, uF: 1e-6, nF: 1e-9, pF: 1e-12 };
        return (value * units[fromUnit]) / units[toUnit];
    }
  
    // Illumination Intensity Converter
    illuminationIntensityConverter(value, fromUnit, toUnit) {
        const units = { lux: 1, ftc: 10.76391 };
        return (value * units[fromUnit]) / units[toUnit];
    }
}