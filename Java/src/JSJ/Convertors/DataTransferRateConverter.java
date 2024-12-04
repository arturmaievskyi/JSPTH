package JSJ.Convertors;

// File: DataTransferRateConverter.java
public class DataTransferRateConverter {

    private static final double BPS_TO_KBPS = 0.001;
    private static final double BPS_TO_MBPS = 1e-6;
    private static final double BPS_TO_GBPS = 1e-9;

    public static double bitsToKilobits(double bps) {
        return bps * BPS_TO_KBPS;
    }

    public static double bitsToMegabits(double bps) {
        return bps * BPS_TO_MBPS;
    }

    public static double bitsToGigabits(double bps) {
        return bps * BPS_TO_GBPS;
    }

}
