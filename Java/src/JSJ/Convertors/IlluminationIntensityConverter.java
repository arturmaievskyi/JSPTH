package JSJ.Convertors;

// File: IlluminationIntensityConverter.java
public class IlluminationIntensityConverter {

    private static final double LUX_TO_FOOT_CANDLE = 0.092903;

    public static double luxToFootCandles(double lux) {
        return lux * LUX_TO_FOOT_CANDLE;
    }

    public static double footCandlesToLux(double footCandles) {
        return footCandles / LUX_TO_FOOT_CANDLE;
    }

}
