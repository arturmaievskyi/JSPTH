public class MassConverter {

    private static final double GRAMS_TO_KILOGRAMS = 0.001;
    private static final double GRAMS_TO_POUNDS = 0.00220462;
    private static final double GRAMS_TO_OUNCES = 0.035274;

    public static double gramsToKilograms(double grams) {
        return grams * GRAMS_TO_KILOGRAMS;
    }

    public static double gramsToPounds(double grams) {
        return grams * GRAMS_TO_POUNDS;
    }

    public static double gramsToOunces(double grams) {
        return grams * GRAMS_TO_OUNCES;
    }
}