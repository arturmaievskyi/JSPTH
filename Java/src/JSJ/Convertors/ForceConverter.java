package JSJ.Convertors;

// File: ForceConverter.java
public class ForceConverter {

    private static final double NEWTON_TO_DYNE = 100000;
    private static final double NEWTON_TO_POUND_FORCE = 0.224809;
    private static final double NEWTON_TO_KILOGRAM_FORCE = 0.101972;

    public static double newtonsToDynes(double newtons) {
        return newtons * NEWTON_TO_DYNE;
    }

    public static double newtonsToPoundForce(double newtons) {
        return newtons * NEWTON_TO_POUND_FORCE;
    }

    public static double newtonsToKilogramForce(double newtons) {
        return newtons * NEWTON_TO_KILOGRAM_FORCE;
    }


}
