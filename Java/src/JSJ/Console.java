package JSJ;

import java.util.Scanner;

class Console {
    private static final Scanner scanner = new Scanner(System.in);

    /**
     * Logs a message to the console.
     *
     * @param message The message to log.
     */
    public static void log(String message) {
        System.out.println(message);
    }

    /**
     * Prompts the user and retrieves a string input.
     *
     * @param prompt The message to display before input.
     * @return The user's input as a string.
     */
    public static String Get(String prompt) {
        log(prompt);
        return scanner.nextLine();
    }

    /**
     * Prompts the user and retrieves an integer input.
     * Retries until a valid integer is provided.
     *
     * @param prompt The message to display before input.
     * @return The user's input as an integer.
     */
    public static int IntGet(String prompt) {
        while (true) {
            log(prompt);
            try {
                return Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                log("Invalid input. Please enter a valid integer.");
            }
        }
    }

    /**
     * Prompts the user and retrieves a floating-point input.
     * Retries until a valid float is provided.
     *
     * @param prompt The message to display before input.
     * @return The user's input as a float.
     */
    public static float FloatGet(String prompt) {
        while (true) {
            log(prompt);
            try {
                return Float.parseFloat(scanner.nextLine());
            } catch (NumberFormatException e) {
                log("Invalid input. Please enter a valid floating-point number.");
            }
        }
    }

    /**
     * Prompts the user and retrieves a double input.
     * Retries until a valid double is provided.
     *
     * @param prompt The message to display before input.
     * @return The user's input as a double.
     */
    public static double DoubleGet(String prompt) {
        while (true) {
            log(prompt);
            try {
                return Double.parseDouble(scanner.nextLine());
            } catch (NumberFormatException e) {
                log("Invalid input. Please enter a valid double.");
            }
        }
    }

    /**
     * Closes the scanner. Should be called before application termination.
     */
    public static void close() {
        scanner.close();
    }
}