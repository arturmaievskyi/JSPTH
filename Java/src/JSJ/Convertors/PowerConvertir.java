// File: PowerConverter.java

package JSJ.Convertors;

public class PowerConverter {

    private static final double WATT_TO_KILOWATT = 0.001;
    private static final double WATT_TO_HORSEPOWER = 0.00134102;
    private static final double WATT_TO_BTU_PER_HOUR = 3.41214;

    public static double wattsToKilowatts(double watts) {
        return watts * WATT_TO_KILOWATT;
    }

    public static double wattsToHorsepower(double watts) {
        return watts * WATT_TO_HORSEPOWER;
    }

    public static double wattsToBTUPerHour(double watts) {
        return watts * WATT_TO_BTU_PER_HOUR;
    }
}
