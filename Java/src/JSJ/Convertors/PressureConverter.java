package JSJ.Convertors;

public class PressureConverter {

    private static final double PASCAL_TO_BAR = 0.00001;
    private static final double PASCAL_TO_ATM = 0.00000986923;
    private static final double PASCAL_TO_PSI = 0.000145038;

    public static double pascalsToBars(double pascals) {
        return pascals * PASCAL_TO_BAR;
    }

    public static double pascalsToAtmospheres(double pascals) {
        return pascals * PASCAL_TO_ATM;
    }

    public static double pascalsToPsi(double pascals) {
        return pascals * PASCAL_TO_PSI;
    }
}