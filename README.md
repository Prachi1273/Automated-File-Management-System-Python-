# 🚀 SmartSysMaint – Intelligent System Automation Suite

> **A Python-based automation suite for file organization, backup management, system auditing, cleanup, and storage monitoring.**

SmartSysMaint is a modular command-line automation tool that simplifies repetitive file system and maintenance tasks. It combines file organization, duplicate detection, versioned backups, temporary file cleanup, folder health auditing, and system monitoring into a single extensible application.

The project was built with a strong focus on **automation, safety, maintainability, and real-world system administration practices**.

---

# 📌 Description

Managing files manually becomes inefficient as systems grow. Download folders become cluttered, duplicate files waste storage, temporary files accumulate over time, and backups are often neglected.

SmartSysMaint automates these routine maintenance tasks while ensuring operations remain **safe, traceable, and configurable** through logging, backup versioning, and modular architecture.

---

# 🎯 Problem Statement

Everyday computer systems suffer from several common issues:

- Unorganized files scattered across directories
- Duplicate files consuming storage
- Temporary files reducing available disk space
- Missing or outdated backups
- Lack of folder health and permission monitoring
- Manual maintenance that is repetitive and error-prone

SmartSysMaint solves these problems by providing an automated and centralized maintenance solution.

---

# ✨ Features

## 📂 File Management
- Organize files by extension
- Automatically organize screenshots
- Auto rename messy filenames
- Create nested folder structures
- Generate employee/project folders

---

## 🗄️ Storage & Cleanup

- Detect duplicate files using **SHA-256 hashing**
- Quarantine duplicate files safely
- Clean temporary files
- Archive old files
- Archive and rotate log files

---

## 💾 Backup Management

- Timestamp-based backups
- Automatic backup versioning
- Configurable retention policy
- Multiple source directory support

---

## 🖥️ System Monitoring

- Folder health auditing
- Read/Write permission verification
- Disk space monitoring
- Folder size visualization
- System information collection

---

## 📊 Reporting

- File inventory snapshot
- Automated report folder generation
- Detailed logging for every operation

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.x |
| File Operations | os, shutil |
| Date & Time | datetime |
| Hashing | hashlib |
| Logging | logging |
| Regular Expressions | re |
| Collections | defaultdict |
| CLI | Command Line Interface |
| Configuration | config.py |

---

# 🏗 Project Architecture

```
SmartSysMaint/
│
├── organizer/
│   ├── organizer.py
│   ├── screenshot_manager.py
│   ├── renamer.py
│
├── cleanup/
│   ├── duplicate_finder.py
│   ├── temp_file_cleaner.py
│
├── backup/
│   ├── versioning.py
│
├── system_info/
│   ├── auditor.py
│   ├── disk_monitor.py
│   ├── inventory.py
│
├── reports/
├── logs/
├── config.py
├── main.py
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/SmartSysMaint.git

cd SmartSysMaint
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📋 Requirements

- Python 3.10+
- pip
- Windows / Linux / macOS

Python Libraries Used

```
os
shutil
hashlib
logging
datetime
collections
re
platform
psutil
```

---

# ▶️ Usage

Run the application

```bash
python main.py
```

Main Menu

```
1. Organize Files by Type
2. Organize Screenshots
3. Archive Old Files
4. Find Duplicate Files
5. Generate Employee Folders
6. Create Nested Folder Structure
7. Rotate Log Files
8. Audit Folder Health
9. Visualize Folder Sizes
10. Collect System Information
11. Monitor Disk Space
12. Backup with Versioning
13. Auto Rename Files
14. Clean Temporary Files
15. File Inventory Snapshot
16. Generate Reports
0. Exit
```

---

# 📸 Example Output 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/885b60ab-f35b-41a3-bb18-350e1ed0cd70" />


---

# 💻 Sample Output

```
Starting duplicate file scan...

Duplicate Found

Original:
Documents/report.pdf

Duplicate:
Downloads/report_copy.pdf

Moved duplicate file to quarantine.

Duplicate scan completed.

Total duplicates quarantined: 1
```

---

# 🔄 Workflow

```
          User
            │
            ▼
      SmartSysMaint CLI
            │
            ▼
     Select Automation Task
            │
            ▼
   Validate Configuration
            │
            ▼
   Perform File/System Operation
            │
            ▼
     Logging & Error Handling
            │
            ▼
   Generate Report / Output
```

---

# 🧠 Engineering Highlights

Unlike a basic automation script, SmartSysMaint follows several software engineering practices:

✅ Modular Architecture

Each automation feature is implemented independently for better maintainability.

---

✅ Configuration Driven Design

All configurable values such as directories, file mappings, backup limits, and extensions are stored separately from business logic.

---

✅ Safety First Automation

- Dry Run Mode
- Duplicate Quarantine
- Backup Versioning
- Permission Auditing

No critical operation is performed blindly.

---

✅ Performance Optimization

Duplicate detection uses a **two-stage approach**:

1. Group files by size
2. Hash only files with identical sizes

This significantly reduces unnecessary hashing.

---

✅ Memory Efficient Processing

Large files are hashed in **4 KB chunks** instead of loading them entirely into memory.

---

✅ Production Style Logging

Every operation is logged for:

- Debugging
- Auditing
- Error Tracking
- Monitoring

---

# 🚧 Challenges Faced

- Preventing accidental data loss
- Efficient duplicate detection
- Handling permission errors
- Managing backup versions
- Designing reusable modules
- Avoiding hardcoded paths
- Cross-platform path handling

---

# 🚀 Future Improvements

- GUI using Tkinter or PyQt
- Watchdog for real-time folder monitoring
- Cloud backup support
- SQLite backup history
- Email notifications
- Multi-threaded file processing
- YAML/JSON based configuration
- REST API support
- Docker deployment
- Scheduler using Cron/Task Scheduler

---

# 📚 Learning Outcomes

Through this project I gained practical experience in:

- Python File System Automation
- Modular Software Design
- Configuration Driven Development
- Logging & Debugging
- SHA-256 Hashing
- Backup Versioning
- Regular Expressions
- Exception Handling
- Memory Efficient File Processing
- Recursive Directory Traversal
- OS Level File Operations
- System Monitoring

---

# 💼 Why This Project Matters

SmartSysMaint demonstrates more than Python programming.

It showcases the ability to:

- Design maintainable software
- Build reusable automation tools
- Write production-oriented code
- Handle real-world edge cases
- Think beyond simple scripting

The project reflects practices commonly used in system administration, DevOps automation, and backend utility development.

---

# 👨‍💻 Author

**Prachi Barve**


---

# 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and contribute.

---

⭐ If you found this project useful, consider giving it a star!
