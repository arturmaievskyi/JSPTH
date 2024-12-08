use std::fs::{self, File};
use std::io::{self, Read, Write};
use std::path::Path;

struct FileManager;

impl FileManager {
    /// Reads the contents of a file and returns it as a String.
    fn read_file(file_path: &str) -> Result<String, io::Error> {
        let mut file = File::open(file_path)?;
        let mut contents = String::new();
        file.read_to_string(&mut contents)?;
        Ok(contents)
    }

    /// Writes the given content to a file, overwriting if the file already exists.
    fn write_file(file_path: &str, content: &str) -> Result<(), io::Error> {
        let mut file = File::create(file_path)?;
        file.write_all(content.as_bytes())?;
        Ok(())
    }

    /// Appends the given content to a file, creating the file if it doesn't exist.
    fn append_to_file(file_path: &str, content: &str) -> Result<(), io::Error> {
        let mut file = OpenOptions::new()
            .create(true)
            .append(true)
            .open(file_path)?;
        file.write_all(content.as_bytes())?;
        Ok(())
    }

    /// Deletes the specified file.
    fn delete_file(file_path: &str) -> Result<(), io::Error> {
        fs::remove_file(file_path)?;
        Ok(())
    }

    /// Checks if a file exists at the given path.
    fn file_exists(file_path: &str) -> bool {
        Path::new(file_path).exists()
    }
}