package JSJ.Convertors;

// File: CapacitanceConverter.java
public class CapacitanceConverter {

    private static final double FARAD_TO_MICROFARAD = 1e6;
    private static final double FARAD_TO_NANOFARAD = 1e9;
    private static final double FARAD_TO_PICOFARAD = 1e12;

    public static double faradsToMicrofarads(double farads) {
        return farads * FARAD_TO_MICROFARAD;
    }

    public static double faradsToNanofarads(double farads) {
        return farads * FARAD_TO_NANOFARAD;
    }

    public static double faradsToPicofarads(double farads) {
        return farads * FARAD_TO_PICOFARAD;
    }


}
