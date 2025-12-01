# SmartSysMaint/system_info/visualizer.py

import os
import logging

def get_folder_size(path):
    """Recursively calculates the size of a folder."""
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size_bytes):
    """Formats size in a human-readable format."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024**2:
        return f"{round(size_bytes/1024, 2)} KB"
    elif size_bytes < 1024**3:
        return f"{round(size_bytes/1024**2, 2)} MB"
    else:
        return f"{round(size_bytes/1024**3, 2)} GB"

def visualize_folder_sizes(target_dir, max_bar_width=50):
    """
    Displays a simple CLI bar chart of the sizes of subdirectories.
    """
    logging.info(f"Visualizing folder sizes for '{target_dir}'...")
    
    subdirs = [d for d in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, d))]
    
    if not subdirs:
        logging.info("No subdirectories to visualize.")
        return

    dir_sizes = {}
    for subdir in subdirs:
        path = os.path.join(target_dir, subdir)
        dir_sizes[subdir] = get_folder_size(path)

    # Find max size for scaling the bar chart
    max_size = max(dir_sizes.values()) if dir_sizes else 1

    print("\n--- Folder Size Visualization ---")
    for name, size in sorted(dir_sizes.items(), key=lambda item: item[1], reverse=True):
        bar_length = int((size / max_size) * max_bar_width) if max_size > 0 else 0
        bar = '█' * bar_length
        print(f"{name:<30} | {bar:<{max_bar_width}} | {format_size(size)}")
    print("---------------------------------\n")

    logging.info("Folder size visualization complete.")
