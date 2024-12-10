import re

# Regular expression to capture lines with 'WARNING' or 'ERROR'
pattern = r"(WARNING|ERROR)"

# Path to the log file (example)
log_file_path = "./logger.log"

# Open and read the log file
with open(log_file_path, "r") as file:
    for line in file:
        # Search for lines containing 'WARNING' or 'ERROR'
        if re.search(pattern, line):
            print(line.strip())  # Print matching lines without extra spaces