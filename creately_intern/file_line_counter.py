import os
import logging
from datetime import datetime

def setup_logging():
    """Configures logging to store output in a log file."""
    log_filename = "file_processing.log"
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def count_lines(file_path):
    """Counts the number of lines in a file (ignoring empty lines) and logs the result."""
    if not os.path.isfile(file_path):
        logging.error(f"File not found: {file_path}")
        print(f"Error: File '{file_path}' not found.")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            # Count lines that are not empty
            line_count = sum(1 for line in file if line.strip())
        
        log_message = f"Processed file: {file_path} | Total lines (excluding empty): {line_count}"
        logging.info(log_message)
        print(log_message)
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        print(f"Error processing file: {e}")

def process_multiple_files(file_paths):
    """Processes multiple files and counts lines for each."""
    for file_path in file_paths:
        count_lines(file_path)

if __name__ == "__main__":
    setup_logging()
    file_paths_input = input("Enter the file paths (comma separated): ")
    # Split input by commas and strip any extra spaces
    file_paths = [path.strip() for path in file_paths_input.split(',')]
    process_multiple_files(file_paths)
