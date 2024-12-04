package JSJ.Convertors;

public class FuelEfficiencyConverter {

    private static final double MPG_TO_KML = 0.425144;
    private static final double KML_TO_L100KM = 100;
    private static final double L100KM_TO_MPG = 235.214;

    public static double mpgToKmPerLiter(double mpg) {
        return mpg * MPG_TO_KML;
    }

    public static double kmPerLiterToL100Km(double kml) {
        return KML_TO_L100KM / kml;
    }

    public static double l100KmToMpg(double l100km) {
        return L100KM_TO_MPG / l100km;
    }
}