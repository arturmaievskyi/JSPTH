struct PowerConverter;

impl PowerConverter {
    fn watts_to_horsepower(watts: f64) -> f64 {
        watts / 745.7
    }

    fn horsepower_to_watts(horsepower: f64) -> f64 {
        horsepower * 745.7
    }
}

struct ForceConverter;

impl ForceConverter {
    fn newtons_to_pounds_force(newtons: f64) -> f64 {
        newtons * 0.224809
    }

    fn pounds_force_to_newtons(pounds: f64) -> f64 {
        pounds / 0.224809
    }
}

struct TorqueConverter;

impl TorqueConverter {
    fn newton_meters_to_foot_pounds(newton_meters: f64) -> f64 {
        newton_meters * 0.737562
    }

    fn foot_pounds_to_newton_meters(foot_pounds: f64) -> f64 {
        foot_pounds / 0.737562
    }
}

struct DensityConverter;

impl DensityConverter {
    fn kilograms_per_cubic_meter_to_pounds_per_cubic_foot(kg_m3: f64) -> f64 {
        kg_m3 * 0.062428
    }

    fn pounds_per_cubic_foot_to_kilograms_per_cubic_meter(pounds: f64) -> f64 {
        pounds / 0.062428
    }
}

struct LuminanceConverter;

impl LuminanceConverter {
    fn candelas_per_square_meter_to_nits(cd_m2: f64) -> f64 {
        cd_m2 // 1:1 conversion, as candelas/m² and nits are identical
    }

    fn nits_to_candelas_per_square_meter(nits: f64) -> f64 {
        nits // 1:1 conversion, as candelas/m² and nits are identical
    }
}
struct FuelEfficiencyConverter;

impl FuelEfficiencyConverter {
    fn mpg_to_kpl(mpg: f64) -> f64 {
        mpg * 0.425144
    }

    fn kpl_to_mpg(kpl: f64) -> f64 {
        kpl / 0.425144
    }
}

struct RadioactivityConverter;

impl RadioactivityConverter {
    fn becquerels_to_curie(becquerels: f64) -> f64 {
        becquerels / 3.7e10
    }

    fn curie_to_becquerels(curie: f64) -> f64 {
        curie * 3.7e10
    }
}

struct DataTransferRateConverter;

impl DataTransferRateConverter {
    fn bits_per_second_to_bytes_per_second(bps: f64) -> f64 {
        bps / 8.0
    }

    fn bytes_per_second_to_bits_per_second(bps: f64) -> f64 {
        bps * 8.0
    }
}

struct CapacitanceConverter;

impl CapacitanceConverter {
    fn farads_to_microfarads(farads: f64) -> f64 {
        farads * 1e6
    }

    fn microfarads_to_farads(microfarads: f64) -> f64 {
        microfarads / 1e6
    }
}

struct IlluminationIntensityConverter;

impl IlluminationIntensityConverter {
    fn lux_to_foot_candles(lux: f64) -> f64 {
        lux * 0.092903
    }

    fn foot_candles_to_lux(fc: f64) -> f64 {
        fc / 0.092903
    }
}

struct PowerConverter;

impl PowerConverter {
    fn watts_to_horsepower(watts: f64) -> f64 {
        watts / 745.7
    }

    fn horsepower_to_watts(horsepower: f64) -> f64 {
        horsepower * 745.7
    }

    fn kilowatts_to_horsepower(kilowatts: f64) -> f64 {
        kilowatts * 1.34102
    }

    fn horsepower_to_kilowatts(horsepower: f64) -> f64 {
        horsepower / 1.34102
    }
}

struct ForceConverter;

impl ForceConverter {
    fn newtons_to_pounds_force(newtons: f64) -> f64 {
        newtons * 0.224809
    }

    fn pounds_force_to_newtons(pounds: f64) -> f64 {
        pounds / 0.224809
    }
}

struct TorqueConverter;

impl TorqueConverter {
    fn newton_meters_to_foot_pounds(newton_meters: f64) -> f64 {
        newton_meters * 0.737562
    }

    fn foot_pounds_to_newton_meters(foot_pounds: f64) -> f64 {
        foot_pounds / 0.737562
    }
}

struct DensityConverter;

impl DensityConverter {
    fn kilograms_per_cubic_meter_to_pounds_per_cubic_foot(kg_m3: f64) -> f64 {
        kg_m3 * 0.062428
    }

    fn pounds_per_cubic_foot_to_kilograms_per_cubic_meter(pounds: f64) -> f64 {
        pounds / 0.062428
    }
}

struct LuminanceConverter;

impl LuminanceConverter {
    fn candelas_per_square_meter_to_nits(cd_m2: f64) -> f64 {
        cd_m2 // 1:1 conversion; both units are equivalent
    }

    fn nits_to_candelas_per_square_meter(nits: f64) -> f64 {
        nits // 1:1 conversion; both units are equivalent
    }
}

struct FuelEfficiencyConverter;

impl FuelEfficiencyConverter {
    fn mpg_to_kpl(mpg: f64) -> f64 {
        mpg * 0.425144
    }

    fn kpl_to_mpg(kpl: f64) -> f64 {
        kpl / 0.425144
    }

    fn l_per_100km_to_mpg(l_per_100km: f64) -> f64 {
        235.214 / l_per_100km
    }

    fn mpg_to_l_per_100km(mpg: f64) -> f64 {
        235.214 / mpg
    }
}

struct RadioactivityConverter;

impl RadioactivityConverter {
    fn becquerels_to_curie(becquerels: f64) -> f64 {
        becquerels / 3.7e10
    }

    fn curie_to_becquerels(curie: f64) -> f64 {
        curie * 3.7e10
    }
}

struct DataTransferRateConverter;

impl DataTransferRateConverter {
    fn bits_per_second_to_bytes_per_second(bps: f64) -> f64 {
        bps / 8.0
    }

    fn bytes_per_second_to_bits_per_second(bps: f64) -> f64 {
        bps * 8.0
    }

    fn megabits_per_second_to_megabytes_per_second(mbps: f64) -> f64 {
        mbps / 8.0
    }

    fn megabytes_per_second_to_megabits_per_second(mbps: f64) -> f64 {
        mbps * 8.0
    }
}

struct CapacitanceConverter;

impl CapacitanceConverter {
    fn farads_to_microfarads(farads: f64) -> f64 {
        farads * 1e6
    }

    fn microfarads_to_farads(microfarads: f64) -> f64 {
        microfarads / 1e6
    }

    fn farads_to_nanofarads(farads: f64) -> f64 {
        farads * 1e9
    }

    fn nanofarads_to_farads(nanofarads: f64) -> f64 {
        nanofarads / 1e9
    }
}

struct IlluminationIntensityConverter;

impl IlluminationIntensityConverter {
    fn lux_to_foot_candles(lux: f64) -> f64 {
        lux * 0.092903
    }

    fn foot_candles_to_lux(fc: f64) -> f64 {
        fc / 0.092903
    }
}

struct DistanceConverter;

impl DistanceConverter {
    fn kilometers_to_miles(km: f64) -> f64 {
        km * 0.621371
    }

    fn miles_to_kilometers(miles: f64) -> f64 {
        miles / 0.621371
    }

    fn meters_to_feet(meters: f64) -> f64 {
        meters * 3.28084
    }

    fn feet_to_meters(feet: f64) -> f64 {
        feet / 3.28084
    }
}

struct TemperatureConverter;

impl TemperatureConverter {
    fn celsius_to_fahrenheit(celsius: f64) -> f64 {
        celsius * 9.0 / 5.0 + 32.0
    }

    fn fahrenheit_to_celsius(fahrenheit: f64) -> f64 {
        (fahrenheit - 32.0) * 5.0 / 9.0
    }

    fn celsius_to_kelvin(celsius: f64) -> f64 {
        celsius + 273.15
    }

    fn kelvin_to_celsius(kelvin: f64) -> f64 {
        kelvin - 273.15
    }
}

struct PressureConverter;

impl PressureConverter {
    fn pascals_to_atmospheres(pascals: f64) -> f64 {
        pascals / 101325.0
    }

    fn atmospheres_to_pascals(atm: f64) -> f64 {
        atm * 101325.0
    }

    fn psi_to_pascals(psi: f64) -> f64 {
        psi * 6894.76
    }

    fn pascals_to_psi(pascals: f64) -> f64 {
        pascals / 6894.76
    }
}

struct EnergyConverter;

impl EnergyConverter {
    fn joules_to_calories(joules: f64) -> f64 {
        joules / 4.184
    }

    fn calories_to_joules(calories: f64) -> f64 {
        calories * 4.184
    }

    fn kilowatt_hours_to_joules(kwh: f64) -> f64 {
        kwh * 3.6e6
    }

    fn joules_to_kilowatt_hours(joules: f64) -> f64 {
        joules / 3.6e6
    }
}

struct FrequencyConverter;

impl FrequencyConverter {
    fn hertz_to_kilohertz(hz: f64) -> f64 {
        hz / 1000.0
    }

    fn kilohertz_to_hertz(khz: f64) -> f64 {
        khz * 1000.0
    }

    fn hertz_to_megahertz(hz: f64) -> f64 {
        hz / 1e6
    }

    fn megahertz_to_hertz(mhz: f64) -> f64 {
        mhz * 1e6
    }
}
struct StorageConverter;

impl StorageConverter {
    fn bytes_to_kilobytes(bytes: f64) -> f64 {
        bytes / 1024.0
    }

    fn kilobytes_to_bytes(kb: f64) -> f64 {
        kb * 1024.0
    }

    fn megabytes_to_gigabytes(mb: f64) -> f64 {
        mb / 1024.0
    }

    fn gigabytes_to_megabytes(gb: f64) -> f64 {
        gb * 1024.0
    }
}

struct AreaConverter;

impl AreaConverter {
    fn square_meters_to_square_feet(sq_meters: f64) -> f64 {
        sq_meters * 10.7639
    }

    fn square_feet_to_square_meters(sq_feet: f64) -> f64 {
        sq_feet / 10.7639
    }

    fn hectares_to_acres(hectares: f64) -> f64 {
        hectares * 2.47105
    }

    fn acres_to_hectares(acres: f64) -> f64 {
        acres / 2.47105
    }
}

struct VolumeConverter;

impl VolumeConverter {
    fn liters_to_gallons(liters: f64) -> f64 {
        liters * 0.264172
    }

    fn gallons_to_liters(gallons: f64) -> f64 {
        gallons / 0.264172
    }

    fn cubic_meters_to_cubic_feet(cubic_meters: f64) -> f64 {
        cubic_meters * 35.3147
    }

    fn cubic_feet_to_cubic_meters(cubic_feet: f64) -> f64 {
        cubic_feet / 35.3147
    }
}

struct SpeedConverter;

impl SpeedConverter {
    fn kilometers_per_hour_to_miles_per_hour(kph: f64) -> f64 {
        kph * 0.621371
    }

    fn miles_per_hour_to_kilometers_per_hour(mph: f64) -> f64 {
        mph / 0.621371
    }

    fn meters_per_second_to_kilometers_per_hour(mps: f64) -> f64 {
        mps * 3.6
    }

    fn kilometers_per_hour_to_meters_per_second(kph: f64) -> f64 {
        kph / 3.6
    }
}

struct MassConverter;

impl MassConverter {
    fn kilograms_to_pounds(kg: f64) -> f64 {
        kg * 2.20462
    }

    fn pounds_to_kilograms(pounds: f64) -> f64 {
        pounds / 2.20462
    }

    fn grams_to_ounces(grams: f64) -> f64 {
        grams * 0.035274
    }

    fn ounces_to_grams(ounces: f64) -> f64 {
        ounces / 0.035274
    }
}