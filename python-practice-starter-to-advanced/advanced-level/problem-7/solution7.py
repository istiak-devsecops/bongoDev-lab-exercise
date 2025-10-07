import os
import time

WATCH_DIR = "./watched_folder"
seen_files = set(os.listdir(WATCH_DIR))

print("Watching for new .txt files...")

while True:
    current_files = set(os.listdir(WATCH_DIR))
    new_files = current_files - seen_files
    txt_files = [f for f in new_files if f.endswith(".txt")]

    for file in txt_files:
        print(f"New .txt file detected: {file}")

    seen_files = current_files
    time.sleep(2)  # Check every 2 seconds