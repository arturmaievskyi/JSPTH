package JSJ.Convertors;

public class DistanceConverter {

    private static final double METER_TO_KILOMETER = 0.001;
    private static final double METER_TO_MILE = 0.000621371;
    private static final double METER_TO_FOOT = 3.28084;

    public static double metersToKilometers(double meters) {
        return meters * METER_TO_KILOMETER;
    }

    public static double metersToMiles(double meters) {
        return meters * METER_TO_MILE;
    }

    public static double metersToFeet(double meters) {
        return meters * METER_TO_FOOT;
    }
}