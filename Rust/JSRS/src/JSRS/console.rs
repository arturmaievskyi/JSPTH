use std::io::{self, Write};

struct Console;

impl Console {
    /// Logs a message to the console.
    fn log(message: &str) {
        println!("{}", message);
    }

    /// Prompts the user and retrieves a raw string input.
    fn get(prompt: &str) -> String {
        print!("{}", prompt);
        io::stdout().flush().unwrap(); // Ensure the prompt is printed before waiting for input
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        input.trim().to_string()
    }

    /// Prompts the user and retrieves an integer input.
    fn int_get(prompt: &str) -> Result<i32, String> {
        let input = Self::get(prompt);
        input.parse::<i32>().map_err(|_| format!("Invalid integer: '{}'", input))
    }

    /// Prompts the user and retrieves a floating-point number.
    fn float_get(prompt: &str) -> Result<f64, String> {
        let input = Self::get(prompt);
        input.parse::<f64>().map_err(|_| format!("Invalid float: '{}'", input))
    }
}
