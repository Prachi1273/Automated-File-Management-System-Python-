
import os

# --- IMPORTANT: SET YOUR TARGET DIRECTORIES HERE ---
# The main folder to perform most operations on (organizing, cleaning, etc.)
# Example for Windows: "C:/Users/YourUser/Downloads"
# Example for macOS/Linux: "/Users/YourUser/Downloads"
TARGET_DIR = "/home/prachi/Desktop/AMBK" # <--- CHANGE THIS

# --- FILE ORGANIZER CONFIGURATION ---
# Sub-directory within TARGET_DIR where organized files will go.
ORGANIZED_DIR = os.path.join(TARGET_DIR, "Organized")

# Mapping of file extensions to folder names
FILE_TYPE_MAPPINGS = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents", ".xlsx": "Documents",
    ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos",
    ".mp3": "Music", ".wav": "Music",
    ".zip": "Archives", ".rar": "Archives",
    ".py": "Scripts", ".js": "Scripts", ".sh": "Scripts",
    # Add more mappings as needed
}
SCREENSHOTS_DIR = os.path.join(ORGANIZED_DIR, "Screenshots")

# --- ARCHIVER & CLEANUP CONFIGURATION ---
ARCHIVE_DIR = os.path.join(TARGET_DIR, "Archive_Old_Files")
LOG_ARCHIVE_DIR = os.path.join(os.path.dirname(__file__), "logs", "archive")
DUPLICATE_QUARANTINE_DIR = os.path.join(TARGET_DIR, "Duplicate_Files")

# Age in days for a file to be considered "old"
OLD_FILE_THRESHOLD_DAYS = 90
LOG_ARCHIVE_THRESHOLD_DAYS = 30

# File extensions to be considered "temporary"
TEMP_FILE_EXTENSIONS = [".tmp", ".bak", ".log", ".temp"]

# --- BACKUP & VERSIONING CONFIGURATION ---
# List of folders you want to back up
DIRECTORIES_TO_BACKUP = [
    "/path/to/important/project1", # <--- CHANGE THIS
    "/path/to/another/important/folder"  # <--- CHANGE THIS
]
BACKUP_DESTINATION = "/path/to/your/backup/drive" # <--- CHANGE THIS
MAX_BACKUP_VERSIONS = 5 # Number of old backups to keep

# --- FOLDER GENERATION CONFIGURATION ---
# Base path for generating new employee/project folders
PROJECT_BASE_PATH = os.path.join(TARGET_DIR, "Projects")

# --- REPORTING CONFIGURATION ---
INVENTORY_REPORT_PATH = os.path.join(TARGET_DIR, "file_inventory_report.txt")
REPORT_FOLDER_BASE_PATH = os.path.join(TARGET_DIR, "Automated_Reports")

# --- DISK SPACE MONITOR CONFIGURATION ---
# Path to monitor disk space for (e.g., '/' for root on Linux, 'C:' on Windows)
DISK_TO_MONITOR = "/"
# Warn if free space is below this percentage
DISK_SPACE_WARNING_THRESHOLD_PERCENT = 15

# --- FOLDER HEALTH AUDITOR ---
# List of folders to check for existence and permissions
FOLDERS_TO_AUDIT = [
    TARGET_DIR,
    BACKUP_DESTINATION,
    PROJECT_BASE_PATH
]
