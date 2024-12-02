public class SpeedConverter {

    private static final double MPS_TO_KPH = 3.6;
    private static final double MPS_TO_MPH = 2.23694;

    public static double metersPerSecondToKilometersPerHour(double mps) {
        return mps * MPS_TO_KPH;
    }

    public static double metersPerSecondToMilesPerHour(double mps) {
        return mps * MPS_TO_MPH;
    }
}