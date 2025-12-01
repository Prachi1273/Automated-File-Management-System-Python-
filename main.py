# SmartSysMaint/main.py

import logging
import os
import sys
from datetime import datetime

from colorama import Fore, Style, init

# Import all feature modules
from organizer import file_organizer, folder_generator, renamer
from cleanup import archiver, duplicate_finder, temp_file_cleaner
from backup import versioning
from system_info import auditor, collector, inventory, visualizer
import config

# Initialize colorama
init(autoreset=True)

# --- Logging Setup ---
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "app.log")),
        logging.StreamHandler(sys.stdout)  # Also print logs to console
    ]
)

def print_menu():
    """Prints the main menu of the application."""
    print(Fore.CYAN + "\n--- SmartSysMaint Automation Suite ---")
    print(Fore.YELLOW + "1.  Organize Files by Type")
    print(Fore.YELLOW + "2.  Organize Screenshots")
    print(Fore.YELLOW + "3.  Archive Old Files")
    print(Fore.YELLOW + "4.  Find & Quarantine Duplicate Files")
    print(Fore.YELLOW + "5.  Generate Employee/Project Folders")
    print(Fore.YELLOW + "6.  Create Nested Folder Structure")
    print(Fore.YELLOW + "7.  Archive & Rotate Log Files")
    print(Fore.YELLOW + "8.  Audit Folder Health & Permissions")
    print(Fore.YELLOW + "9.  Visualize Folder Sizes (CLI)")
    print(Fore.YELLOW + "10. Collect and Display System Info")
    print(Fore.YELLOW + "11. Monitor Disk Space")
    print(Fore.YELLOW + "12. Create Backup with Versioning")
    print(Fore.YELLOW + "13. Auto-Rename Messy Filenames")
    print(Fore.YELLOW + "14. Clean Up Temporary Files")
    print(Fore.YELLOW + "15. Create File Inventory Snapshot")
    print(Fore.YELLOW + "16. Generate Automated Report Folder")
    print(Fore.RED + "0.  Exit")
    print(Style.RESET_ALL)

def run_task(task_function, *args, **kwargs):
    """Decorator to log start and end of a task."""
    logging.info(f"--- Starting task: {task_function.__name__} ---")
    try:
        task_function(*args, **kwargs)
        logging.info(f"--- Successfully completed task: {task_function.__name__} ---")
    except Exception as e:
        logging.error(f"--- Task failed: {task_function.__name__} with error: {e} ---", exc_info=True)

def main():
    """Main function to run the script runner."""
    if not os.path.exists(config.TARGET_DIR) or config.TARGET_DIR == "/path/to/your/target/folder":
        logging.error(f"Configuration Error: TARGET_DIR is not set or does not exist. Please edit config.py.")
        print(Fore.RED + "CRITICAL: Please set the TARGET_DIR in config.py before running the application.")
        return

    while True:
        print_menu()
        choice = input(Fore.GREEN + "Enter your choice: ")

        if choice == '1':
            run_task(file_organizer.organize_files_by_type, config.TARGET_DIR)
        elif choice == '2':
            run_task(file_organizer.organize_screenshots, config.TARGET_DIR)
        elif choice == '3':
            run_task(archiver.archive_old_files, config.TARGET_DIR)
        elif choice == '4':
            run_task(duplicate_finder.find_and_quarantine_duplicates, config.TARGET_DIR)
        elif choice == '5':
            run_task(folder_generator.generate_project_structure, config.PROJECT_BASE_PATH, ["Project_Alpha", "Project_Beta"], ["Alice", "Bob"])
        elif choice == '6':
            path = input("Enter base path for nested folders (e.g., /tmp/test): ")
            structure = input("Enter structure (e.g., YYYY/MM/DD): ")
            run_task(folder_generator.create_nested_folders, path, structure)
        elif choice == '7':
            run_task(archiver.archive_log_files, "logs")
        elif choice == '8':
            run_task(auditor.audit_folder_health, config.FOLDERS_TO_AUDIT)
        elif choice == '9':
            run_task(visualizer.visualize_folder_sizes, config.TARGET_DIR)
        elif choice == '10':
            run_task(collector.display_system_info)
        elif choice == '11':
            run_task(collector.monitor_disk_space, config.DISK_TO_MONITOR)
        elif choice == '12':
            run_task(versioning.create_backup, config.DIRECTORIES_TO_BACKUP, config.BACKUP_DESTINATION)
        elif choice == '13':
            run_task(renamer.auto_rename_files, config.TARGET_DIR)
        elif choice == '14':
            run_task(temp_file_cleaner.cleanup_temp_files, config.TARGET_DIR, dry_run=False)
        elif choice == '15':
            run_task(inventory.create_file_inventory, config.TARGET_DIR, config.INVENTORY_REPORT_PATH)
        elif choice == '16':
            run_task(folder_generator.create_automated_report_folder, config.REPORT_FOLDER_BASE_PATH)
        elif choice == '0':
            logging.info("Exiting application.")
            break
        else:
            logging.warning(f"Invalid choice: {choice}")
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
