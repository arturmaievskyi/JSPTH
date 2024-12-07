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