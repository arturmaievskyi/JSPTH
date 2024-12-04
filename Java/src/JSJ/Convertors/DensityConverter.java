// File: DensityConverter.java
package JSJ.Convertors;

public class DensityConverter {

    private static final double KG_PER_M3_TO_G_PER_CM3 = 0.001;
    private static final double KG_PER_M3_TO_LB_PER_FT3 = 0.062428;

    public static double kgPerM3ToGPerCm3(double kgPerM3) {
        return kgPerM3 * KG_PER_M3_TO_G_PER_CM3;
    }

    public static double kgPerM3ToLbPerFt3(double kgPerM3) {
        return kgPerM3 * KG_PER_M3_TO_LB_PER_FT3;
    }
}
