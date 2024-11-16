
import os

def count_files_in_directory(directory):
    total_files = 0

    # Traverse the directory tree
    for root, dirs, files in os.walk(directory):
        print(f"Found {len(files)} files in directory: {root}")
        total_files += len(files)

    return total_files

# Usage example:
directory_path = 'JSPTH'  # Replace with your directory path
file_count = count_files_in_directory(directory_path)
print(f"\nTotal number of files: {file_count}\n")