# SmartSysMaint/organizer/renamer.py

import os
import re
import logging
import config

def auto_rename_files(target_dir):
    """
    Renames files with spaces or special characters to a clean, URL-safe format.
    Example: "My Messy File Name 1.txt" -> "my_messy_file_name_1.txt"
    """
    logging.info(f"Starting to rename messy files in '{target_dir}'...")
    files_renamed = 0
    for filename in os.listdir(target_dir):
        if os.path.isfile(os.path.join(target_dir, filename)):
            name, ext = os.path.splitext(filename)
            
            # Replace spaces with underscores and remove special characters
            clean_name = name.lower().strip()
            clean_name = re.sub(r'\s+', '_', clean_name)
            clean_name = re.sub(r'[^\w-]', '', clean_name)
            
            new_filename = f"{clean_name}{ext}"

            if new_filename != filename:
                try:
                    os.rename(os.path.join(target_dir, filename), os.path.join(target_dir, new_filename))
                    logging.info(f"Renamed '{filename}' to '{new_filename}'")
                    files_renamed += 1
                except OSError as e:
                    logging.error(f"Could not rename '{filename}'. Maybe a file with the new name already exists. Error: {e}")

    logging.info(f"File renaming complete. Renamed {files_renamed} files.")
