# SmartSysMaint/system_info/inventory.py

import os
import logging
from datetime import datetime

def create_file_inventory(target_dir, report_path):
    """
    Generates a text report listing all files, their sizes, and modification dates.
    """
    logging.info(f"Creating file inventory for '{target_dir}'...")
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"File Inventory Report for: {target_dir}\n")
            f.write(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-" * 50 + "\n")
            f.write(f"{'Path':<70} {'Size (KB)':>15} {'Modified Date':>20}\n")
            f.write("-" * 50 + "\n")

            file_count = 0
            for dirpath, _, filenames in os.walk(target_dir):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        stats = os.stat(filepath)
                        size_kb = round(stats.st_size / 1024, 2)
                        mod_time = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d')
                        relative_path = os.path.relpath(filepath, target_dir)

                        f.write(f"{relative_path:<70} {size_kb:>15} {mod_time:>20}\n")
                        file_count += 1
                    except OSError:
                        continue
            
            f.write("-" * 50 + "\n")
            f.write(f"Total files found: {file_count}\n")
            
        logging.info(f"Successfully created file inventory report at '{report_path}'.")

    except IOError as e:
        logging.error(f"Failed to write inventory report to '{report_path}': {e}")
