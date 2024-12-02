package JSJ.Convertors;

public class VolumeConverter {

    private static final double LITER_TO_ML = 1000;
    private static final double LITER_TO_CUBIC_METER = 0.001;
    private static final double LITER_TO_GALLON = 0.264172;

    public static double litersToMilliliters(double liters) {
        return liters * LITER_TO_ML;
    }

    public static double litersToCubicMeters(double liters) {
        return liters * LITER_TO_CUBIC_METER;
    }

    public static double litersToGallons(double liters) {
        return liters * LITER_TO_GALLON;
    }
}