import os
import shutil
import time

def organize_files():
    # Path to your Downloads folder
    path = r"C:\Users\Wei Jun\Downloads"
    items = os.listdir(path)
    folder_names = set()

    # Step 1: Identify extensions and create folders
    for item in items:
        if os.path.isfile(os.path.join(path, item)):  # Check if it's a file
            ext = os.path.splitext(item)[1][1:]  # Get file extension (e.g., 'txt')
            if ext:
                folder_names.add(ext)

    for folder_name in folder_names:
        folder_path = os.path.join(path, folder_name)
        if not os.path.exists(folder_path):  # Create folder if it doesn't exist
            os.makedirs(folder_path)

    # Step 2: Move files into their respective folders
    for item in items:
        if os.path.isfile(os.path.join(path, item)):  # Check if it's a file
            ext = os.path.splitext(item)[1][1:]  # Get file extension
            if ext:
                src = os.path.join(path, item)  # Source file path
                dest = os.path.join(path, ext, item)  # Destination folder path
                shutil.move(src, dest)  # Move the file

if __name__ == "__main__":
    # Continuously monitor the Downloads folder
    print("Monitoring Downloads folder. Press Ctrl+C to stop.")
    try:
        while True:
            organize_files()  # Organize files
            time.sleep(10)   # Wait 10 seconds before checking again
    except KeyboardInterrupt:
        print("\nStopping monitoring.")
