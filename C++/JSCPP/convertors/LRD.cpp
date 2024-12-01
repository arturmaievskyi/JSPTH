#include <cmath>
#include <stdexcept>

class UnitConverters {
public:
    // Luminance Converter
    class LuminanceConverter {
    public:
        // Convert candela per square meter (cd/m^2) to nits (same unit)
        static double candela_per_square_meter_to_nits(double cd_per_m2) {
            return cd_per_m2; // Both units are equivalent
        }

        // Convert nits to candela per square meter (cd/m^2)
        static double nits_to_candela_per_square_meter(double nits) {
            return nits; // Both units are equivalent
        }

        // Convert candela per square meter (cd/m^2) to foot-lamberts
        static double candela_per_square_meter_to_foot_lamberts(double cd_per_m2) {
            return cd_per_m2 * 0.2919;
        }

        // Convert foot-lamberts to candela per square meter (cd/m^2)
        static double foot_lamberts_to_candela_per_square_meter(double foot_lamberts) {
            return foot_lamberts / 0.2919;
        }
    };

    // Radioactivity Converter
    class RadioactivityConverter {
    public:
        // Convert becquerels (Bq) to curies (Ci)
        static double becquerels_to_curie(double becquerels) {
            return becquerels / 3.7e10;
        }

        // Convert curies (Ci) to becquerels (Bq)
        static double curie_to_becquerels(double curie) {
            return curie * 3.7e10;
        }

        // Convert becquerels (Bq) to rutherfords (Rd)
        static double becquerels_to_rutherford(double becquerels) {
            return becquerels / 1e6;
        }

        // Convert rutherfords (Rd) to becquerels (Bq)
        static double rutherford_to_becquerels(double rutherford) {
            return rutherford * 1e6;
        }
    };

    // Data Transfer Rate Converter
    class DataTransferRateConverter {
    public:
        // Convert bits per second (bps) to kilobits per second (kbps)
        static double bits_per_second_to_kilobits_per_second(double bps) {
            return bps / 1000.0;
        }

        // Convert kilobits per second (kbps) to bits per second (bps)
        static double kilobits_per_second_to_bits_per_second(double kbps) {
            return kbps * 1000.0;
        }

        // Convert bits per second (bps) to megabits per second (Mbps)
        static double bits_per_second_to_megabits_per_second(double bps) {
            return bps / 1e6;
        }

        // Convert megabits per second (Mbps) to bits per second (bps)
        static double megabits_per_second_to_bits_per_second(double mbps) {
            return mbps * 1e6;
        }

        // Convert megabits per second (Mbps) to gigabits per second (Gbps)
        static double megabits_per_second_to_gigabits_per_second(double mbps) {
            return mbps / 1000.0;
        }

        // Convert gigabits per second (Gbps) to megabits per second (Mbps)
        static double gigabits_per_second_to_megabits_per_second(double gbps) {
            return gbps * 1000.0;
        }
    };
};
