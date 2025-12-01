# SmartSysMaint/cleanup/duplicate_finder.py

import os
import hashlib
import logging
from collections import defaultdict
import shutil
import config

def hash_file(filepath):
    """Calculates the SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except IOError:
        logging.error(f"Could not read file for hashing: {filepath}")
        return None

def find_and_quarantine_duplicates(target_dir):
    """
    Finds duplicate files based on size and hash, then moves them to a quarantine folder.
    """
    logging.info(f"Starting duplicate file scan in '{target_dir}'...")
    if not os.path.exists(config.DUPLICATE_QUARANTINE_DIR):
        os.makedirs(config.DUPLICATE_QUARANTINE_DIR)
        logging.info(f"Created duplicate quarantine directory: {config.DUPLICATE_QUARANTINE_DIR}")

    files_by_size = defaultdict(list)
    files_by_hash = defaultdict(list)
    
    # First pass: group files by size
    for dirpath, _, filenames in os.walk(target_dir):
        # Exclude our own special directories from the scan
        if config.ORGANIZED_DIR in dirpath or \
           config.ARCHIVE_DIR in dirpath or \
           config.DUPLICATE_QUARANTINE_DIR in dirpath:
            continue
            
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(filepath)
                files_by_size[size].append(filepath)
            except OSError:
                continue

    # Second pass: for files of the same size, compare hashes
    duplicates_found = 0
    for size, files in files_by_size.items():
        if len(files) > 1:
            for filepath in files:
                file_hash = hash_file(filepath)
                if file_hash:
                    files_by_hash[file_hash].append(filepath)
    
    # Identify and move duplicates
    for file_hash, files in files_by_hash.items():
        if len(files) > 1:
            original = files.pop(0) # Keep the first one
            logging.warning(f"Duplicate set found. Original: '{original}'. Duplicates: {files}")
            for duplicate_path in files:
                try:
                    shutil.move(duplicate_path, config.DUPLICATE_QUARANTINE_DIR)
                    logging.info(f"Moved duplicate '{duplicate_path}' to quarantine.")
                    duplicates_found += 1
                except shutil.Error as e:
                    logging.error(f"Failed to move duplicate '{duplicate_path}': {e}")
    
    logging.info(f"Duplicate scan complete. Quarantined {duplicates_found} files.")
