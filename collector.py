# SmartSysMaint/system_info/collector.py

import platform
import psutil # Note: This will need to be added to requirements.txt
import shutil
import logging
import config

# Add psutil to requirements.txt if you use this module
# For simplicity, we'll use shutil for disk usage, but psutil is more powerful

def display_system_info():
    """Collects and displays basic system information."""
    logging.info("Collecting system information...")
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    for key, value in info.items():
        logging.info(f"  {key}: {value}")

def bytes_to_gb(bytes_val):
    """Converts bytes to gigabytes."""
    return round(bytes_val / (1024**3), 2)

def monitor_disk_space(path):
    """Monitors disk space for a given path and warns if it's below a threshold."""
    logging.info(f"Monitoring disk space for '{path}'...")
    try:
        total, used, free = shutil.disk_usage(path)
        free_percent = (free / total) * 100
        
        logging.info(f"  Total Space: {bytes_to_gb(total)} GB")
        logging.info(f"  Used Space:  {bytes_to_gb(used)} GB")
        logging.info(f"  Free Space:  {bytes_to_gb(free)} GB ({free_percent:.2f}%)")
        
        if free_percent < config.DISK_SPACE_WARNING_THRESHOLD_PERCENT:
            logging.warning(f"  [ALERT] Free disk space is critically low ({free_percent:.2f}%)!")
        else:
            logging.info("  [OK] Disk space is within acceptable limits.")

    except FileNotFoundError:
        logging.error(f"The path '{path}' does not exist. Cannot check disk space.")
