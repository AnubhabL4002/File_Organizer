import os
import shutil

# Define the source folder and folder mapping
source_folder = "E:/Py-Organization_Test"

folders = {
    "Music": ["mp3", "wav", "flac"],
    "Pictures": ["jpg", "jpeg", "png", "gif", "bmp"],
    "Videos": ["mp4", "mkv", "avi", "mov"],
    "Codes": ["c", "py", "cpp", "js", "html", "css", "java"],
    "Others": []  # For files with unknown extensions
}

# Create the target folders
for folder in folders:
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

# Process files in the root of the source folder
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue

    # Extract file extension
    ext = file.split(".")[-1].lower()

    # Determine the destination folder
    for folder, extensions in folders.items():
        if ext in extensions:
            dest_folder = folder
            break
    else:
        dest_folder = "Others"

    # Move file to the appropriate folder
    dest_path = os.path.join(source_folder, dest_folder)
    new_name = f"{len(os.listdir(dest_path)) + 1:03}_{file}"
    shutil.move(file_path, os.path.join(dest_path, new_name))
    print(f"Moved {file} to {dest_folder}/{new_name}")

# Reorganize files from existing subfolders
for folder_name in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, folder_name)

    # Skip if it's not a folder
    if not os.path.isdir(folder_path):
        continue

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Extract file extension
        ext = file.split(".")[-1].lower()

        # Determine the destination folder
        for folder, extensions in folders.items():
            if ext in extensions:
                dest_folder = folder
                break
        else:
            dest_folder = "Others"

        # Move file if it's not already in the correct folder
        dest_path = os.path.join(source_folder, dest_folder)
        new_name = f"{len(os.listdir(dest_path)) + 1:03}_{file}"

        if folder_name != dest_folder:  # Avoid moving files already in the correct folder
            shutil.move(file_path, os.path.join(dest_path, new_name))
            print(f"Moved {file} to {dest_folder}/{new_name}")

print("Files reorganized successfully!")
