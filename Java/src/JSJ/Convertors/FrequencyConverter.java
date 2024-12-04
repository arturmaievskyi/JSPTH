package JSJ.Convertors;

// File: FrequencyConverter.java
public class FrequencyConverter {

    private static final double HERTZ_TO_KHZ = 0.001;
    private static final double HERTZ_TO_MHZ = 0.000001;
    private static final double HERTZ_TO_GHZ = 0.000000001;

    public static double hertzToKilohertz(double hertz) {
        return hertz * HERTZ_TO_KHZ;
    }

    public static double hertzToMegahertz(double hertz) {
        return hertz * HERTZ_TO_MHZ;
    }

    public static double hertzToGigahertz(double hertz) {
        return hertz * HERTZ_TO_GHZ;
    }


}
