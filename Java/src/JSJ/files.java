// File: FileUtils.java
package JSJ;
import java.io.*;
import java.nio.file.*;

public class files {

    /**
     * Writes content to a file. Overwrites if the file already exists.
     *
     * @param filePath The file path where content should be written.
     * @param content The content to write to the file.
     * @throws IOException If an IO error occurs during the operation.
     */
    public static void writeToFile(String filePath, String content) throws IOException {
        Files.write(Paths.get(filePath), content.getBytes());
    }

    /**
     * Reads content from a file.
     *
     * @param filePath The file path to read from.
     * @return The content of the file as a string.
     * @throws IOException If an IO error occurs or the file doesn't exist.
     */
    public static String readFromFile(String filePath) throws IOException {
        return Files.readString(Paths.get(filePath));
    }

    /**
     * Appends content to a file. Creates the file if it doesn't exist.
     *
     * @param filePath The file path where content should be appended.
     * @param content The content to append to the file.
     * @throws IOException If an IO error occurs during the operation.
     */
    public static void appendToFile(String filePath, String content) throws IOException {
        Files.write(Paths.get(filePath), content.getBytes(), StandardOpenOption.CREATE, StandardOpenOption.APPEND);
    }

    /**
     * Deletes a file.
     *
     * @param filePath The file path of the file to delete.
     * @return True if the file was successfully deleted, false otherwise.
     */
    public static boolean deleteFile(String filePath) {
        try {
            return Files.deleteIfExists(Paths.get(filePath));
        } catch (IOException e) {
            System.err.println("Error deleting file: " + e.getMessage());
            return false;
        }
    }

    /**
     * Example usage of FileUtils methods.
     */
    public static void main(String[] args) {
        String filePath = "example.txt";

        try {
            // Write to file
            writeToFile(filePath, "Hello, world!\n");

            // Append to file
            appendToFile(filePath, "This is an appended line.\n");

            // Read from file
            String content = readFromFile(filePath);
            System.out.println("File Content:\n" + content);

            // Delete file
            boolean deleted = deleteFile(filePath);
            System.out.println("File deleted: " + deleted);

        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
