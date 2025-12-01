# SmartSysMaint/cleanup/archiver.py

import os
import shutil
import time
import logging
import zipfile
import config

def archive_old_files(target_dir):
    """
    Moves files older than a specified threshold to an archive directory.
    """
    logging.info(f"Starting to archive old files from '{target_dir}'...")
    if not os.path.exists(config.ARCHIVE_DIR):
        os.makedirs(config.ARCHIVE_DIR)
        logging.info(f"Created archive directory: {config.ARCHIVE_DIR}")
    
    threshold_seconds = config.OLD_FILE_THRESHOLD_DAYS * 24 * 60 * 60
    now = time.time()
    files_archived = 0

    for filename in os.listdir(target_dir):
        source_path = os.path.join(target_dir, filename)
        if os.path.isfile(source_path):
            file_mod_time = os.path.getmtime(source_path)
            if (now - file_mod_time) > threshold_seconds:
                shutil.move(source_path, os.path.join(config.ARCHIVE_DIR, filename))
                logging.info(f"Archived old file: '{filename}'")
                files_archived += 1

    logging.info(f"Archiving complete. Archived {files_archived} files.")

def archive_log_files(log_dir):
    """
    Finds log files older than a threshold, compresses them, and moves them to an archive.
    """
    logging.info(f"Starting log archiving in '{log_dir}'...")
    if not os.path.exists(config.LOG_ARCHIVE_DIR):
        os.makedirs(config.LOG_ARCHIVE_DIR)
        logging.info(f"Created log archive directory: {config.LOG_ARCHIVE_DIR}")

    threshold_seconds = config.LOG_ARCHIVE_THRESHOLD_DAYS * 24 * 60 * 60
    now = time.time()
    logs_archived = 0

    for filename in os.listdir(log_dir):
        if filename.endswith(".log"):
            source_path = os.path.join(log_dir, filename)
            file_mod_time = os.path.getmtime(source_path)

            if (now - file_mod_time) > threshold_seconds:
                zip_filename = f"{filename}_{time.strftime('%Y-%m-%d')}.zip"
                zip_path = os.path.join(config.LOG_ARCHIVE_DIR, zip_filename)
                
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(source_path, os.path.basename(source_path))
                
                os.remove(source_path)
                logging.info(f"Compressed and archived log file '{filename}' to '{zip_path}'")
                logs_archived += 1

    logging.info(f"Log archiving complete. Archived {logs_archived} logs.")
    
