# SmartSysMaint/backup/versioning.py

import os
import shutil
import logging
from datetime import datetime
import config

def create_backup(source_dirs, dest_dir):
    """
    Creates a timestamped backup of source directories to a destination.
    Also manages old versions, keeping only the specified number.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        logging.info(f"Created backup destination directory: {dest_dir}")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    for source_dir in source_dirs:
        if not os.path.exists(source_dir):
            logging.warning(f"Source directory for backup does not exist: {source_dir}. Skipping.")
            continue
            
        base_name = os.path.basename(os.path.normpath(source_dir))
        backup_name = f"{base_name}_{timestamp}"
        backup_path = os.path.join(dest_dir, backup_name)

        logging.info(f"Backing up '{source_dir}' to '{backup_path}'...")
        try:
            shutil.copytree(source_dir, backup_path)
            logging.info(f"Backup successful for '{source_dir}'.")
            
            # Manage versions for this specific source directory
            manage_versions(dest_dir, base_name)
        except Exception as e:
            logging.error(f"Failed to back up '{source_dir}': {e}")

def manage_versions(backup_dir, source_base_name):
    """
    Deletes the oldest backups if the number of versions exceeds the maximum allowed.
    """
    backups = [d for d in os.listdir(backup_dir) if d.startswith(source_base_name)]
    backups.sort(reverse=True) # Sorts descending, newest first

    if len(backups) > config.MAX_BACKUP_VERSIONS:
        backups_to_delete = backups[config.MAX_BACKUP_VERSIONS:]
        logging.info(f"Found {len(backups_to_delete)} old backup(s) to delete for '{source_base_name}'.")
        for old_backup in backups_to_delete:
            path_to_delete = os.path.join(backup_dir, old_backup)
            try:
                shutil.rmtree(path_to_delete)
                logging.info(f"Deleted old backup: {path_to_delete}")
            except OSError as e:
                logging.error(f"Failed to delete old backup '{path_to_delete}': {e}")
