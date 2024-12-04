package JSJ.Convertors;


// File: RadioactivityConverter.java
public class RadioactivityConverter {

    private static final double BQ_TO_CI = 2.7e-11;
    private static final double BQ_TO_RD = 1e6;

    public static double becquerelsToCuries(double bq) {
        return bq * BQ_TO_CI;
    }

    public static double becquerelsToRutherfords(double bq) {
        return bq / BQ_TO_RD;
    }
}
