# SmartSysMaint/system_info/auditor.py

import os
import logging
import config

def audit_folder_health(folders_to_audit):
    """
    Checks if specified folders exist and if the script has read/write permissions.
    """
    logging.info("Starting folder health and permission audit...")
    for folder_path in folders_to_audit:
        # Check existence
        if not os.path.exists(folder_path):
            logging.error(f"[FAIL] Path does not exist: '{folder_path}'")
            continue
        if not os.path.isdir(folder_path):
            logging.warning(f"[FAIL] Path is not a directory: '{folder_path}'")
            continue
            
        logging.info(f"[OK] Path exists: '{folder_path}'")
        
        # Check permissions
        can_read = os.access(folder_path, os.R_OK)
        can_write = os.access(folder_path, os.W_OK)
        
        if can_read:
            logging.info(f"  [OK] Read permissions are set for '{folder_path}'.")
        else:
            logging.error(f"  [FAIL] Read permissions are MISSING for '{folder_path}'.")
            
        if can_write:
            logging.info(f"  [OK] Write permissions are set for '{folder_path}'.")
        else:
            logging.warning(f"  [WARN] Write permissions are MISSING for '{folder_path}'. This might cause issues.")
            
    logging.info("Folder health audit complete.")
