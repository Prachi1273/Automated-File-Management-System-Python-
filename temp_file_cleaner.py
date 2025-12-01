# SmartSysMaint/cleanup/temp_file_cleaner.py

import os
import logging
import config

def cleanup_temp_files(target_dir, dry_run=True):
    """
    Finds and deletes files with temporary extensions.
    """
    action = "Would delete" if dry_run else "Deleting"
    logging.info(f"Starting temporary file cleanup in '{target_dir}' (Dry Run: {dry_run})...")
    files_cleaned = 0
    
    for dirpath, _, filenames in os.walk(target_dir):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in config.TEMP_FILE_EXTENSIONS):
                filepath = os.path.join(dirpath, filename)
                logging.info(f"{action} temporary file: {filepath}")
                if not dry_run:
                    try:
                        os.remove(filepath)
                        files_cleaned += 1
                    except OSError as e:
                        logging.error(f"Failed to delete {filepath}: {e}")

    logging.info(f"Temporary file cleanup complete. {'Found' if dry_run else 'Deleted'} {files_cleaned} files.")
