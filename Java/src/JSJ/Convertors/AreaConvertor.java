public class AreaConverter {

    private static final double SQM_TO_SQFT = 10.7639;
    private static final double SQM_TO_SQYD = 1.19599;
    private static final double SQM_TO_ACRE = 0.000247105;
    private static final double SQM_TO_SQKM = 0.000001;

    public static double squareMetersToSquareFeet(double sqm) {
        return sqm * SQM_TO_SQFT;
    }

    public static double squareMetersToSquareYards(double sqm) {
        return sqm * SQM_TO_SQYD;
    }

    public static double squareMetersToAcres(double sqm) {
        return sqm * SQM_TO_ACRE;
    }

    public static double squareMetersToSquareKilometers(double sqm) {
        return sqm * SQM_TO_SQKM;
    }
}