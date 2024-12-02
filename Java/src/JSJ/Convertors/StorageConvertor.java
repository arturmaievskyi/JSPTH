public class StorageConverter {

    private static final long BYTE = 1;
    private static final long KILOBYTE = 1024 * BYTE;
    private static final long MEGABYTE = 1024 * KILOBYTE;
    private static final long GIGABYTE = 1024 * MEGABYTE;
    private static final long TERABYTE = 1024 * GIGABYTE;

    public static double bytesToKilobytes(long bytes) {
        return (double) bytes / KILOBYTE;
    }

    public static double bytesToMegabytes(long bytes) {
        return (double) bytes / MEGABYTE;
    }

    public static double bytesToGigabytes(long bytes) {
        return (double) bytes / GIGABYTE;
    }

    public static double bytesToTerabytes(long bytes) {
        return (double) bytes / TERABYTE;
    }
}