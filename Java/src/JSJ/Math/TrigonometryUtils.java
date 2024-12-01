package JSJ.Math;

public class TrigonometryUtils {

    // Sine of an angle (in radians)
    public static double sine(double angle) {
        return Math.sin(angle);
    }

    // Cosine of an angle (in radians)
    public static double cosine(double angle) {
        return Math.cos(angle);
    }

    // Tangent of an angle (in radians)
    public static double tangent(double angle) {
        return Math.tan(angle);
    }

    // Arcsine (inverse sine), returns value in radians
    public static double arcsine(double value) {
        return Math.asin(value);
    }

    // Arccosine (inverse cosine), returns value in radians
    public static double arccosine(double value) {
        return Math.acos(value);
    }

    // Arctangent (inverse tangent), returns value in radians
    public static double arctangent(double value) {
        return Math.atan(value);
    }

    // Law of Cosines: c² = a² + b² - 2ab * cos(γ)
    public static double lawOfCosines(double a, double b, double gamma) {
        return Math.sqrt(a * a + b * b - 2 * a * b * Math.cos(gamma));
    }

    // Law of Sines: (a / sin(α)) = (b / sin(β)) = (c / sin(γ))
    public static double lawOfSines(double a, double alpha, double b) {
        return b * Math.sin(alpha) / a;
    }

    // Secant (reciprocal of cosine)
    public static double secant(double angle) {
        return 1 / Math.cos(angle);
    }

    // Cosecant (reciprocal of sine)
    public static double cosecant(double angle) {
        return 1 / Math.sin(angle);
    }

    // Cotangent (reciprocal of tangent)
    public static double cotangent(double angle) {
        return 1 / Math.tan(angle);
    }

    // Sine of a sum of two angles: sin(α + β) = sin(α) * cos(β) + cos(α) * sin(β)
    public static double sineSum(double alpha, double beta) {
        return Math.sin(alpha) * Math.cos(beta) + Math.cos(alpha) * Math.sin(beta);
    }

    // Cosine of a sum of two angles: cos(α + β) = cos(α) * cos(β) - sin(α) * sin(β)
    public static double cosineSum(double alpha, double beta) {
        return Math.cos(alpha) * Math.cos(beta) - Math.sin(alpha) * Math.sin(beta);
    }

    // Tangent of a sum of two angles: tan(α + β) = (tan(α) + tan(β)) / (1 - tan(α) * tan(β))
    public static double tangentSum(double alpha, double beta) {
        return (Math.tan(alpha) + Math.tan(beta)) / (1 - Math.tan(alpha) * Math.tan(beta));
    }

    // Sine of double angle: sin(2α) = 2 * sin(α) * cos(α)
    public static double sineDouble(double alpha) {
        return 2 * Math.sin(alpha) * Math.cos(alpha);
    }

    // Cosine of double angle: cos(2α) = cos²(α) - sin²(α)
    public static double cosineDouble(double alpha) {
        return Math.cos(alpha) * Math.cos(alpha) - Math.sin(alpha) * Math.sin(alpha);
    }

    // Tangent of double angle: tan(2α) = 2 * tan(α) / (1 - tan²(α))
    public static double tangentDouble(double alpha) {
        return 2 * Math.tan(alpha) / (1 - Math.pow(Math.tan(alpha), 2));
    }

    // Convert polar coordinates (r, θ) to Cartesian coordinates (x, y)
    public static double[] polarToCartesian(double r, double theta) {
        double x = r * Math.cos(theta);
        double y = r * Math.sin(theta);
        return new double[] { x, y };
    }

    // Convert Cartesian coordinates (x, y) to polar coordinates (r, θ)
    public static double[] cartesianToPolar(double x, double y) {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.atan2(y, x);  // atan2 handles quadrant
        return new double[] { r, theta };
    }
}