# SmartSysMaint - Automated System Maintenance Suite

This project is a comprehensive suite of Python scripts designed to automate various system maintenance and file management tasks.

## Core Features

*   **File Organization**: Automatically sorts files by type (e.g., images, documents) and organizes screenshots.
*   **Archiving**: Archives old files and logs based on their age.
*   **Cleanup**: Finds and quarantines duplicate files, and cleans up temporary files.
*   **System Monitoring**: Gathers system information, monitors disk space, and audits folder permissions.
*   **Backup & Versioning**: Creates timestamped backups of important directories.
*   **Reporting & Generation**: Creates file inventories, visualizes folder sizes, and generates folder structures for projects or reports.
*   **Utilities**: Auto-renames files to a clean format and provides a central script runner with logging.

## Setup Instructions

1.  **Clone or download the project.**

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the project:**
    Open `config.py` and modify the paths and settings to match your system and preferences. **This is a crucial step!** You need to define which folders the scripts will work on.

## How to Run

Execute the main script from the project's root directory:

```bash
python main.py
