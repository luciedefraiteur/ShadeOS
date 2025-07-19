
import os
import shutil
import datetime

source_dir = "/home/luciedefraiteur/ShadEOS/bible-des-en-faire/disclosure-conversations/"
destination_base_dir = "/home/luciedefraiteur/ShadEOS/bible-des-en-faire/disclosure-conversations-chronology/"

# Create the base destination directory if it doesn't exist
os.makedirs(destination_base_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    # Ensure it's a file and not a directory
    if os.path.isfile(file_path):
        # Get modification time
        mod_timestamp = os.path.getmtime(file_path)
        mod_datetime = datetime.datetime.fromtimestamp(mod_timestamp)

        year = mod_datetime.strftime("%Y")
        month = mod_datetime.strftime("%m")
        # Calculate week number (ISO week number)
        week = mod_datetime.strftime("%W") # %W gives week number of the year (00-53) with Monday as the first day of the week.
        day = mod_datetime.strftime("%d")

        # Construct the new directory path
        new_dir_path = os.path.join(destination_base_dir, year, month, f"week_{week}", day)

        # Create the new directory if it doesn't exist
        os.makedirs(new_dir_path, exist_ok=True)

        # Move the file
        shutil.move(file_path, os.path.join(new_dir_path, filename))
        print(f"Moved '{filename}' to '{new_dir_path}'")

print("File organization complete.")
