#include <cmath>
#include <stdexcept>

class UnitConverter {
public:
    // Temperature Converter
    class TemperatureConverter {
    public:
        static double celsius_to_fahrenheit(double celsius) {
            return celsius * 9.0 / 5.0 + 32;
        }

        static double fahrenheit_to_celsius(double fahrenheit) {
            return (fahrenheit - 32) * 5.0 / 9.0;
        }

        static double celsius_to_kelvin(double celsius) {
            return celsius + 273.15;
        }

        static double kelvin_to_celsius(double kelvin) {
            if (kelvin < 0) throw std::invalid_argument("Temperature below absolute zero.");
            return kelvin - 273.15;
        }
    };

    // Distance Converter
    class DistanceConverter {
    public:
        static double meters_to_kilometers(double meters) {
            return meters / 1000.0;
        }

        static double kilometers_to_meters(double kilometers) {
            return kilometers * 1000.0;
        }

        static double miles_to_kilometers(double miles) {
            return miles * 1.60934;
        }

        static double kilometers_to_miles(double kilometers) {
            return kilometers / 1.60934;
        }
    };

    // Speed Converter
    class SpeedConverter {
    public:
        static double meters_per_second_to_kilometers_per_hour(double mps) {
            return mps * 3.6;
        }

        static double kilometers_per_hour_to_meters_per_second(double kph) {
            return kph / 3.6;
        }

        static double miles_per_hour_to_kilometers_per_hour(double mph) {
            return mph * 1.60934;
        }

        static double kilometers_per_hour_to_miles_per_hour(double kph) {
            return kph / 1.60934;
        }
    };

    // Mass Converter
    class MassConverter {
    public:
        static double kilograms_to_grams(double kilograms) {
            return kilograms * 1000.0;
        }

        static double grams_to_kilograms(double grams) {
            return grams / 1000.0;
        }

        static double pounds_to_kilograms(double pounds) {
            return pounds * 0.453592;
        }

        static double kilograms_to_pounds(double kilograms) {
            return kilograms / 0.453592;
        }
    };

    // Area Converter
    class AreaConverter {
    public:
        static double square_meters_to_square_kilometers(double sq_meters) {
            return sq_meters / 1e6;
        }

        static double square_kilometers_to_square_meters(double sq_kilometers) {
            return sq_kilometers * 1e6;
        }

        static double acres_to_square_meters(double acres) {
            return acres * 4046.86;
        }

        static double square_meters_to_acres(double sq_meters) {
            return sq_meters / 4046.86;
        }
    };

    // Volume Converter
    class VolumeConverter {
    public:
        static double liters_to_milliliters(double liters) {
            return liters * 1000.0;
        }

        static double milliliters_to_liters(double milliliters) {
            return milliliters / 1000.0;
        }

        static double gallons_to_liters(double gallons) {
            return gallons * 3.78541;
        }

        static double liters_to_gallons(double liters) {
            return liters / 3.78541;
        }
    };

    // Energy Converter
    class EnergyConverter {
    public:
        static double joules_to_kilojoules(double joules) {
            return joules / 1000.0;
        }

        static double kilojoules_to_joules(double kilojoules) {
            return kilojoules * 1000.0;
        }

        static double calories_to_joules(double calories) {
            return calories * 4.184;
        }

        static double joules_to_calories(double joules) {
            return joules / 4.184;
        }
    };

    // Fuel Efficiency Converter
    class FuelEfficiencyConverter {
    public:
        static double mpg_to_liters_per_100km(double mpg) {
            return 235.214 / mpg;
        }

        static double liters_per_100km_to_mpg(double l_per_100km) {
            return 235.214 / l_per_100km;
        }
    };

    // Pressure Converter
    class PressureConverter {
    public:
        static double pascals_to_atm(double pascals) {
            return pascals / 101325.0;
        }

        static double atm_to_pascals(double atm) {
            return atm * 101325.0;
        }

        static double pascals_to_bar(double pascals) {
            return pascals / 100000.0;
        }

        static double bar_to_pascals(double bar) {
            return bar * 100000.0;
        }
    };
};
