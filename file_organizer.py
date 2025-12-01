# SmartSysMaint/organizer/file_organizer.py

import os
import shutil
import logging
import config

def organize_files_by_type(target_dir):
    """
    Organizes files in a directory into subdirectories based on their file extension.
    """
    logging.info(f"Starting file organization in '{target_dir}'...")
    if not os.path.exists(config.ORGANIZED_DIR):
        os.makedirs(config.ORGANIZED_DIR)
        logging.info(f"Created directory: {config.ORGANIZED_DIR}")

    files_moved = 0
    for filename in os.listdir(target_dir):
        source_path = os.path.join(target_dir, filename)
        if os.path.isfile(source_path):
            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            if extension in config.FILE_TYPE_MAPPINGS:
                folder_name = config.FILE_TYPE_MAPPINGS[extension]
                dest_folder = os.path.join(config.ORGANIZED_DIR, folder_name)

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                    logging.info(f"Created subdirectory: {dest_folder}")

                dest_path = os.path.join(dest_folder, filename)
                shutil.move(source_path, dest_path)
                logging.info(f"Moved '{filename}' to '{dest_folder}'")
                files_moved += 1

    logging.info(f"File organization complete. Moved {files_moved} files.")

def organize_screenshots(target_dir):
    """
    Finds files with 'screenshot' in their name and moves them to a dedicated folder.
    """
    logging.info(f"Starting screenshot organization in '{target_dir}'...")
    if not os.path.exists(config.SCREENSHOTS_DIR):
        os.makedirs(config.SCREENSHOTS_DIR)
        logging.info(f"Created directory: {config.SCREENSHOTS_DIR}")

    files_moved = 0
    for filename in os.listdir(target_dir):
        source_path = os.path.join(target_dir, filename)
        if os.path.isfile(source_path) and "screenshot" in filename.lower():
            dest_path = os.path.join(config.SCREENSHOTS_DIR, filename)
            shutil.move(source_path, dest_path)
            logging.info(f"Moved screenshot '{filename}' to '{config.SCREENSHOTS_DIR}'")
            files_moved += 1

    logging.info(f"Screenshot organization complete. Moved {files_moved} files.")
    
    


'''
import os
import shutil
import logging

# ---------- Configuration ----------
FILE_TYPE = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.txt', '.docx', '.xlsx'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3', '.wav']
}

# Setup logging
logging.basicConfig(
    filename='organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------- Functions ----------

def create_folder(path):
    """Create folder if it doesn't exist."""
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except Exception as e:
        logging.error(f"Failed to create folder {path}: {e}")
        print(f"Error creating folder: {path}")

def get_category(extension):
    """Return the category based on file extension."""
    for category, extensions in FILE_TYPE.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    """Organize files in the specified folder."""
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist. Please check the path.")
        return

    destination_folder = os.path.join(folder_path, 'organized_files')
    create_folder(destination_folder)

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip organized_files folder and category folders inside it
        if (item == 'organized_files') or (os.path.isdir(item_path) and item in FILE_TYPE.keys()):
            continue

        if os.path.isdir(item_path):
            continue  # Skip other folders

        file_ext = os.path.splitext(item)[1]

        category = get_category(file_ext)
        dest_category_folder = os.path.join(destination_folder, category)
        create_folder(dest_category_folder)

        try:
            shutil.move(item_path, dest_category_folder)
            logging.info(f"Moved '{item}' to '{category}' folder.")
            print(f"✅ Moved '{item}' to '{category}' folder.")
        except Exception as e:
            logging.error(f"Failed to move {item}: {e}")
            print(f"Error moving file: {item}")

    print("\n🎉 Organization Complete!")
    logging.info("Organization completed successfully.")

# ---------- Main Execution ----------

if __name__ == "__main__":
    folder_to_organize = input("Enter the path of the folder to organize: ").strip()
    organize_folder(folder_to_organize)




import os
import shutil

# Dictionary to categorize files based on their extensions
FILE_TYPE = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.txt', '.docx', '.xlsx'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3', '.wav']
}

# Step 1: Take input from user for the folder to organize
folder_to_organize = input("Enter the path of folder to organize: ")

# Step 2: Check if folder exists
if not os.path.exists(folder_to_organize):
    print("Folder does not exist. Please check the path.")
    exit()

# Step 3: Define the destination folder to keep organized files
destination_folder = os.path.join(folder_to_organize, 'organized_files')

# Step 4: Create 'organized_files' folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Step 5: Loop through all items in the folder
for item in os.listdir(folder_to_organize):
    item_path = os.path.join(folder_to_organize, item)  # Full path of the item

    # Step 6: Skip the 'organized_files' folder itself or any folders named same as categories
    if (item == 'organized_files') or (os.path.isdir(item_path) and item in FILE_TYPE.keys()):
        continue  # Skip to next item

    # Step 7: Extract the file extension
    file_ext = os.path.splitext(item)[1]

    # Step 8: Flag to track whether the file has been moved
    moved = False

    # Step 9: Loop through categories to check where the file belongs
    for folder_name, extensions in FILE_TYPE.items():
        if file_ext.lower() in extensions:
            dest_folder = os.path.join(destination_folder, folder_name)  # Destination folder for this category

            # Step 10: Create the category folder if it doesn't exist
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            # Step 11: Move the file to the appropriate category folder
            shutil.move(item_path, dest_folder)
            moved = True  # Mark as moved
            print(f"Moved '{item}' to '{folder_name}' folder.")
            break  # No need to check other categories

    # Step 12: If file doesn't match any category, move to 'Others' folder
    if not moved:
        others_folder = os.path.join(destination_folder, 'Others')
        if not os.path.exists(others_folder):
            os.makedirs(others_folder)
        shutil.move(item_path, others_folder)
        print(f"Moved '{item}' to 'Others' folder.")

# Step 13: Final message after all files processed
print("\nOrganization Complete!")
'''
