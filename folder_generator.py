# SmartSysMaint/organizer/folder_generator.py

import os
import logging
from datetime import datetime
import config

def create_nested_folders(base_path, structure):
    """
    Creates a nested folder structure based on a given string like 'YYYY/MM/DD'.
    Replaces placeholders with current date parts.
    """
    now = datetime.now()
    path_to_create = structure.replace("YYYY", now.strftime("%Y")) \
                              .replace("MM", now.strftime("%m")) \
                              .replace("DD", now.strftime("%d"))

    full_path = os.path.join(base_path, path_to_create)
    os.makedirs(full_path, exist_ok=True)
    logging.info(f"Ensured nested folder structure exists: {full_path}")
    return full_path

def generate_project_structure(base_path, project_names, employee_names):
    """
    Generates a standard folder structure for new projects and employees.
    Example: base_path/Project_Name/Employee_Name
    """
    logging.info(f"Generating project structures under '{base_path}'")
    for project in project_names:
        for employee in employee_names:
            path = os.path.join(base_path, project, employee)
            os.makedirs(path, exist_ok=True)
            logging.info(f"Created or verified folder: {path}")

def create_automated_report_folder(base_path):
    """
    Creates a folder for automated reports, named with the current date.
    Example: base_path/Report_YYYY-MM-DD
    """
    today_str = datetime.now().strftime("Report_%Y-%m-%d")
    report_path = os.path.join(base_path, today_str)
    if not os.path.exists(report_path):
        os.makedirs(report_path)
        logging.info(f"Created automated report folder: {report_path}")
    else:
        logging.info(f"Report folder for today already exists: {report_path}")
    return report_path
