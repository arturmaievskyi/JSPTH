package JSJ.Convertors;
// File: TorqueConverter.java
public class TorqueConverter {

    private static final double NEWTON_METER_TO_POUND_FOOT = 0.737562;
    private static final double NEWTON_METER_TO_KILOGRAM_METER = 0.101972;

    public static double newtonMetersToPoundFoot(double newtonMeters) {
        return newtonMeters * NEWTON_METER_TO_POUND_FOOT;
    }

    public static double newtonMetersToKilogramMeter(double newtonMeters) {
        return newtonMeters * NEWTON_METER_TO_KILOGRAM_METER;
    }

    public static void main(String[] args) {
        double newtonMeters = 100; // Example: 100 Newton-Meters
        System.out.println("Pound-Foot: " + newtonMetersToPoundFoot(newtonMeters));
        System.out.println("Kilogram-Meter: " + newtonMetersToKilogramMeter(newtonMeters));
    }
}
