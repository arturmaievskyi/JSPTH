package JSJ.Convertors;

public class LuminanceConverter {

    private static final double CANDELA_M2_TO_LUX = 1; // Approximation for direct conversion
    private static final double CANDELA_M2_TO_FOOT_LAMBERT = 0.2919;

    public static double candelasToLux(double candelas) {
        return candelas * CANDELA_M2_TO_LUX;
    }

    public static double candelasToFootLamberts(double candelas) {
        return candelas * CANDELA_M2_TO_FOOT_LAMBERT;
    }
}