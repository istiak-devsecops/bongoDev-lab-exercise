import re

# Path to the Docker log file
log_path = "docker.log"

# Regex pattern to match error lines with timestamps
pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*(ERROR|Exception)', re.IGNORECASE)

# Read and analyze the log
with open(log_path, 'r') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            print(line.strip())
