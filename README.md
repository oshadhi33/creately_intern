# creately_intern
File Line Counter (Dockerized)

This project provides a simple Python script that counts the number of lines in a given file. The script runs inside a Docker container, processes files from a mounted directory, and logs the results in a human-readable format with timestamps.

🚀 FeaturesWorks with any text-based file Stores results in a log file Runs in a Docker container Automatically processes a file when the container starts

📂 Project Structurecreately_intern/
│── Dockerfile

│── file_line_counter.py

│── input_files/   # Place your input files here

│   ├── sample.txt

│── logs/          # Log files will be saved here🛠 PrerequisitesDocker installed on your system


Python 3 (only needed for local testing, not required if using Docker)

🏗 Build the Docker ImageRun the following command inside the project directory:
docker build -t file_counter .

▶ Run the ContainerRun the following command to execute the script inside Docker:

docker run --rm -v "$(pwd)/input_files:/app/input_files" -v "$(pwd)/logs:/app/logs" file_counterOn Windows (CMD/PowerShell), use absolute paths:

docker run --rm -v "C:\Users\USER\Desktop\creately_intern\input_files:/app/input_files" -v "C:\Users\USER\Desktop\creately_intern\logs:/app/logs" file_counter

📄 Sample Input FileCreate a sample file inside the input_files/ directory:

This is a sample text file.
It contains multiple lines.
Each line will be counted by the script.
Docker mounts this file inside the container.

Make sure the file path is correct.

📜Log File OutputAfter running the container, 
check the log file:

type logs/file_processing.log  # Windows

cat logs/file_processing.log   # Linux/macOS

Expected log format:

2025-03-05 12:30:15 - Processed file: /app/input_files/sample.txt | Total lines: 5

🛑 Stopping the ContainerSince the container runs and exits immediately, you don’t need to manually stop it. 
However, if you run it in detached mode (-d), stop it using:

docker stop <container_id>

🐞 TroubleshootingLog file not found? 
Make sure the logs/ folder exists before running the container:

mkdir logsDocker volume mount issues? Ensure you are using the correct path format for your OS.

Permissions error? Run Docker with administrative privileges.
