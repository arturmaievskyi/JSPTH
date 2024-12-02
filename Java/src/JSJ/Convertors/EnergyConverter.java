package JSJ.Convertors;

public class EnergyConverter {

    private static final double JOULE_TO_CALORIE = 0.239006;
    private static final double JOULE_TO_KWH = 2.77778e-7;
    private static final double JOULE_TO_EV = 6.242e18;

    public static double joulesToCalories(double joules) {
        return joules * JOULE_TO_CALORIE;
    }

    public static double joulesToKilowattHours(double joules) {
        return joules * JOULE_TO_KWH;
    }

    public static double joulesToElectronVolts(double joules) {
        return joules * JOULE_TO_EV;
    }
}