// File: Main.java
import JSJ.Console;

public class Main {
    public static void main(String[] args) {
        Console.log("Hello from Console class!");

        String name = Console.Get("What's your name?");
        int age = Console.IntGet("How old are you?");
        Console.log("Name: " + name + ", Age: " + age);

    }
}
